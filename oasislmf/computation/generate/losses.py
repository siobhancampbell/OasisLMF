__all__ = [
    'GenerateLosses',
    'GenerateLossesDir',
    'GenerateLossesPartial',
    'GenerateLossesOutput',
    'GenerateLossesDeterministic',
    'GenerateLossesDummyModel'
]

import importlib
import io
import json
import multiprocessing
import os
import re
import subprocess
import sys
import warnings
from collections import OrderedDict
from json import JSONDecodeError
from pathlib import Path
from subprocess import CalledProcessError, check_call

import pandas as pd
import numpy as np

from oasis_data_manager.filestore.config import get_storage_from_config_path
from oasis_data_manager.filestore.backends.local import LocalStorage

from ...execution import bash, runner
from ...execution.bash import get_fmcmd, RUNTYPE_GROUNDUP_LOSS, RUNTYPE_INSURED_LOSS, RUNTYPE_REINSURANCE_LOSS
from ...execution.bin import (csv_to_bin, prepare_run_directory,
                              prepare_run_inputs, set_footprint_set, set_vulnerability_set, set_loss_factors_set)
from ...preparation.summaries import generate_summaryxref_files
from ...pytools.fm.financial_structure import create_financial_structure
from oasislmf.pytools.summary.manager import create_summary_object_file
from ...utils.data import (get_dataframe, get_exposure_data, get_json,
                           get_utctimestamp, merge_dataframes, set_dataframe_column_dtypes,
                           analysis_settings_loader, model_settings_loader)
from ...utils.defaults import (EVE_DEFAULT_SHUFFLE, EVE_STD_SHUFFLE, KTOOL_N_FM_PER_LB,
                               KTOOL_N_GUL_PER_LB, KTOOLS_ALLOC_FM_MAX, KTOOLS_ALLOC_GUL_DEFAULT,
                               KTOOLS_ALLOC_GUL_MAX, KTOOLS_ALLOC_IL_DEFAULT,
                               KTOOLS_ALLOC_RI_DEFAULT, KTOOLS_DEBUG, KTOOLS_GUL_LEGACY_STREAM,
                               KTOOLS_MEAN_SAMPLE_IDX, KTOOLS_NUM_PROCESSES,
                               KTOOLS_STD_DEV_SAMPLE_IDX, KTOOLS_TIV_SAMPLE_IDX)
from ...utils.exceptions import OasisException
from ...utils.inputs import str2bool
from ...utils.path import setcwd
from ..base import ComputationStep
from .files import GenerateDummyModelFiles, GenerateDummyOasisFiles

warnings.simplefilter(action='ignore', category=FutureWarning)


class GenerateLossesBase(ComputationStep):
    """
    Base class for Loss generation functions

    Includes methods useful across all GenerateLoss functions
    intended as a common inherited class
    """

    def _get_output_dir(self):
        """
        Set the model run directory to '<cwd>/runs/losses-<timestamp>' if not set
        in arguments

        :return: (str) the model run directory, either given or generated
        """
        if not self.model_run_dir:
            utcnow = get_utctimestamp(fmt='%Y%m%d%H%M%S')
            self.model_run_dir = os.path.join(os.getcwd(), 'runs', 'losses-{}'.format(utcnow))
        if not os.path.exists(self.model_run_dir):
            Path(self.model_run_dir).mkdir(parents=True, exist_ok=True)
        return self.model_run_dir

    def _get_model_runner(self):
        """
        Returns the model runner module, by default this is imported from `oasislmf/execution/runner.py`
        but can be overridden from the conf option `model_package_dir`

        :return: (object) The model runner module, (str) Package Name
        """
        package_name = None
        if self.model_package_dir and os.path.exists(os.path.join(self.model_package_dir, 'supplier_model_runner.py')):
            path, package_name = os.path.split(self.model_package_dir)
            sys.path.append(path)
            return importlib.import_module('{}.supplier_model_runner'.format(package_name)), package_name
        else:
            return runner, package_name

    def _check_ktool_rules(self):
        """
        Check the given ktool allocation rules are within valid ranges
        Raises an `OasisException` if a rules is invalid
        """
        rule_ranges = {
            'ktools_alloc_rule_gul': KTOOLS_ALLOC_GUL_MAX,
            'ktools_alloc_rule_il': KTOOLS_ALLOC_FM_MAX,
            'ktools_alloc_rule_ri': KTOOLS_ALLOC_FM_MAX,
            'ktools_event_shuffle': EVE_STD_SHUFFLE,
            'gulpy_random_generator': 1}

        for rule in rule_ranges:
            rule_val = int(getattr(self, rule))
            if (rule_val < 0) or (rule_val > rule_ranges[rule]):
                raise OasisException(f'Error: {rule}={rule_val} - Not within valid ranges [0..{rule_ranges[rule]}]')

    def _store_run_settings(self, analysis_settings, target_dir):
        """
        Writes the analysis settings file to the `target_dir` path
        """
        with io.open(os.path.join(target_dir, 'analysis_settings.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(analysis_settings, ensure_ascii=False, indent=4))

    def _is_run_settings_stored(self, target_dir):
        """
        Checks if analysis settings file is under target_dir path
        """
        return os.path.isfile(os.path.join(target_dir, 'analysis_settings.json'))

    def _get_num_ri_layers(self, analysis_settings, model_run_fp):
        """
        Find the number of Reinsurance layers based on `'ri_layers.json'`, returns pos int()
        """
        ri_layers = 0
        if analysis_settings.get('ri_output', False) or analysis_settings.get('rl_output', False):
            ri_layers = len(get_json(os.path.join(model_run_fp, 'input', 'ri_layers.json')))
        return ri_layers

    def _get_peril_filter(self, analysis_settings):
        """
        Check the 'analysis_settings' for user set peril filter, if empty return the MDK peril filter
        option
        """
        user_peril_filter = analysis_settings.get('peril_filter', None)
        peril_filter = list(map(str.upper, user_peril_filter if user_peril_filter else self.peril_filter))
        return peril_filter

    def _print_error_logs(self, run_log_fp, e):
        """
        Error handling Method: Call if a run error has accursed,
        * prints ktool log files to logger
        * Raises `OasisException`
        """
        bash_trace_fp = os.path.join(run_log_fp, 'bash.log')
        if os.path.isfile(bash_trace_fp):
            with io.open(bash_trace_fp, 'r', encoding='utf-8') as f:
                self.logger.info('\nBASH_TRACE:\n' + "".join(f.readlines()))

        stderror_fp = os.path.join(run_log_fp, 'stderror.err')
        if os.path.isfile(stderror_fp):
            with io.open(stderror_fp, 'r', encoding='utf-8') as f:
                self.logger.info('\nKTOOLS_STDERR:\n' + "".join(f.readlines()))

        gul_stderror_fp = os.path.join(run_log_fp, 'gul_stderror.err')
        if os.path.isfile(gul_stderror_fp):
            with io.open(gul_stderror_fp, 'r', encoding='utf-8') as f:
                self.logger.info('\nGUL_STDERR:\n' + "".join(f.readlines()))

        self.logger.info('\nSTDOUT:\n' + e.output.decode('utf-8').strip())

        raise OasisException(
            'Ktools run Error: non-zero exit code or error/warning messages detected in STDERR output.\n'
            'Killing all processes. To disable this automated check run with `--ktools-disable-guard`.\n'
            'Logs stored in: {}'.format(run_log_fp)
        )


class GenerateLossesDir(GenerateLossesBase):
    """
    Prepare the loss generation directory

    * converts input `csv` files to ktools binary types
    * links model data to the static directory to the run locations
    * Validates and updates the `analysis_settings.json`
    * Stores the analysis_settings.json in the output directory

    :return: (dict) Updated analysis_settings
    """
    settings_params = [{'name': 'analysis_settings_json', 'loader': analysis_settings_loader, 'user_role': 'user'},
                       {'name': 'model_settings_json', 'loader': model_settings_loader}]

    step_params = [
        # Command line options
        {'name': 'oasis_files_dir', 'flag': '-o', 'is_path': True, 'pre_exist': True,
         'required': True, 'help': 'Path to the directory in which to generate the Oasis files'},
        {'name': 'check_oed', 'type': str2bool, 'const': True, 'nargs': '?', 'default': True, 'help': 'if True check input oed files'},
        {'name': 'analysis_settings_json', 'flag': '-a', 'is_path': True, 'pre_exist': True, 'required': True,
         'help': 'Analysis settings JSON file path'},
        {'name': 'model_storage_json', 'is_path': True, 'pre_exist': True, 'required': False,
         'help': 'Model data storage settings JSON file path'},
        {'name': 'model_settings_json', 'flag': '-M', 'is_path': True, 'pre_exist': False, 'required': False,
         'help': 'Model settings JSON file path'},
        {'name': 'user_data_dir', 'flag': '-D', 'is_path': True, 'pre_exist': False,
         'help': 'Directory containing additional model data files which varies between analysis runs'},
        {'name': 'model_data_dir', 'flag': '-d', 'is_path': True, 'pre_exist': True, 'help': 'Model data directory path'},
        {'name': 'copy_model_data', 'default': False, 'type': str2bool, 'help': 'Copy model data instead of creating symbolic links to it.'},
        {'name': 'model_run_dir', 'flag': '-r', 'is_path': True, 'pre_exist': False, 'help': 'Model run directory path'},
        {'name': 'model_package_dir', 'flag': '-p', 'is_path': True, 'pre_exist': False, 'help': 'Path containing model specific package'},
        {'name': 'ktools_legacy_stream', 'type': str2bool, 'const': True, 'nargs': '?', 'default': KTOOLS_GUL_LEGACY_STREAM,
         'help': 'Run Ground up losses using the older stream type (Compatibility option)'},
        {'name': 'fmpy', 'default': True, 'type': str2bool, 'const': True, 'nargs': '?', 'help': 'use fmcalc python version instead of c++ version'},
        {'name': 'ktools_alloc_rule_il', 'default': KTOOLS_ALLOC_IL_DEFAULT, 'type': int,
         'help': 'Set the fmcalc allocation rule used in direct insured loss'},
        {'name': 'ktools_alloc_rule_ri', 'default': KTOOLS_ALLOC_RI_DEFAULT, 'type': int,
         'help': 'Set the fmcalc allocation rule used in reinsurance'},
        {'name': 'summarypy', 'default': False, 'type': str2bool, 'const': True,
            'nargs': '?', 'help': 'use summarycalc python version instead of c++ version'},
        {'name': 'check_missing_inputs', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'Fail an analysis run if IL/RI is requested without the required generated files.'},

        # Manager only options (pass data directy instead of filepaths)
        {'name': 'verbose', 'default': KTOOLS_DEBUG},

    ]

    def _get_storage_manager(self):
        model_storage = get_storage_from_config_path(
            self.model_storage_json,
            os.path.join(self.model_run_dir, "static"),
        )

        # if not local test the connection to remote storage FS
        if not isinstance(model_storage, LocalStorage):
            try:
                model_storage.listdir()
            except Exception as e:
                raise OasisException('Error: Storage Manager connection issue', e)

        return model_storage

    def __check_for_parquet_output(self, analysis_settings, runtypes):
        """
        Private method to check whether ktools components were linked to third
        party parquet libraries during compilation if user requests parquet
        output.
        """
        for runtype in runtypes:
            for summary in analysis_settings.get(f'{runtype}_summaries', {}):
                if summary.get('ord_output', {}).get('parquet_format'):
                    katparquet_output = subprocess.run(
                        ['katparquet', '-v'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    if not 'Parquet output enabled' in katparquet_output.stderr.decode():
                        raise OasisException(
                            'Parquet output format requested but not supported by ktools components. '
                            'Please set "parquet_format" to false in analysis settings file.'
                        )
                    return  # Only need to find a single request

    def __check_summary_group_support(self, analysis_settings, runtypes):
        """
        Private method to check the max number of summary groups selected.
        If that value is greater than 9 then ktools 'summarycalc' will crash.

        Stop execution if the summarypy flag is not set as True.
        """
        for runtype in runtypes:
            summary_num = len(analysis_settings.get(f'{runtype}_summaries', []))
            if summary_num > 9 and not self.summarypy:
                raise OasisException(
                    'More than 9 summaries groups are not supported in summarycalc.'
                    f'\nEither enable summarypy or reduce the number of groups set in "{runtype}_summaries".'
                    '\nThis can be set using the flag "--summarypy True", or by setting `"summarypy": True` in the oasislmf.json file.'
                )

    def run(self):
        # need to load from exposure data info or recreate it
        model_run_fp = self._get_output_dir()
        model_storage = self._get_storage_manager()

        il = all(p in os.listdir(self.oasis_files_dir) for p in [
            'fm_policytc.csv',
            'fm_profile.csv',
            'fm_programme.csv',
            'fm_xref.csv'])

        ri_dirs = [fn
                   for fn in os.listdir(self.oasis_files_dir) + os.listdir(self.model_run_dir)
                   if re.match(r"RI_\d+$", fn)
                   ]
        ril = any(ri_dirs)

        # Check for missing input files and either warn user or raise exception
        il_missing = self.settings.get('il_output', False) and not il
        ri_missing = self.settings.get('ri_output', False) and not ril
        rl_missing = self.settings.get('rl_output', False) and not ril
        if il_missing or ri_missing or rl_missing:
            missing_input_files = "{} are enabled in the analysis_settings without the generated input files. The 'generate-oasis-files' step should be rerun with account/reinsurance files.".format(
                [
                    "IL" * il_missing, "RI" * ri_missing, "RL" * rl_missing
                ]
            )
            if self.check_missing_inputs:
                raise OasisException(missing_input_files)
            else:
                self.logger.warning(missing_input_files)

        gul_item_stream = (not self.ktools_legacy_stream)
        ri = self.settings.get('ri_output', False) and ril
        rl = self.settings.get('rl_output', False) and ril
        self.logger.info('\nPreparing loss Generation (GUL=True, IL={}, RI={}, RL={})'.format(il, ri, rl))

        runtypes = ['gul'] + ['il'] * il + ['ri'] * ri + ['rl'] * rl
        self.__check_for_parquet_output(self.settings, runtypes)
        self.__check_summary_group_support(self.settings, runtypes)

        prepare_run_directory(
            model_run_fp,
            self.oasis_files_dir,
            self.model_data_dir,
            self.analysis_settings_json,
            user_data_dir=self.user_data_dir,
            ri=ri or rl,
            copy_model_data=self.copy_model_data,
            model_storage_config_fp=self.model_storage_json,
        )

        exposure_data = get_exposure_data(self, add_internal_col=True)
        location_df = exposure_data.get_subject_at_risk_source().dataframe
        account_df = exposure_data.account.dataframe if exposure_data.account else None
        generate_summaryxref_files(
            location_df,
            account_df,
            model_run_fp,
            self.settings,
            gul_item_stream=gul_item_stream,
            il=il,
            ri=ri,
            rl=rl,
            fmpy=self.fmpy
        )

        if not ri and not rl:
            fp = os.path.join(model_run_fp, 'input')
            csv_to_bin(fp, fp, il=il)
        else:
            contents = os.listdir(model_run_fp)
            for fp in [os.path.join(model_run_fp, fn) for fn in contents if re.match(r'RI_\d+$', fn) or re.match(r'input$', fn)]:
                csv_to_bin(fp, fp, il=True, ri=True)

        if not il:
            self.settings['il_output'] = False
            self.settings['il_summaries'] = []

        if not ri:
            self.settings['ri_output'] = False
            self.settings['ri_summaries'] = []

        if not rl:
            self.settings['rl_output'] = False
            self.settings['rl_summaries'] = []

        if not any(self.settings.get(output) for output in ['gul_output', 'il_output', 'ri_output']):
            raise OasisException(
                'No valid output settings in: {}'.format(self.analysis_settings_json))

        # Load default samples if not set in analysis settings
        # Additional check to avoid 0 samples being interpreted as false
        if not self.settings.get('number_of_samples') and self.settings.get('number_of_samples') != 0:
            if not self.model_settings_json:
                raise OasisException("'number_of_samples' not set in analysis_settings and no model_settings.json file provided for a default value.")

            default_model_samples = self.settings.get('model_default_samples')
            if default_model_samples is None:
                raise OasisException(
                    "'number_of_samples' not set in analysis_settings and no default value 'model_default_samples' found in model_settings file.")

            self.logger.info(f"Loaded samples from model_settings file: 'model_default_samples = {default_model_samples}'")
            self.settings['number_of_samples'] = default_model_samples

        prepare_run_inputs(self.settings, model_run_fp, model_storage, ri=ri or rl)

        optional_model_sets = {'footprint_set': set_footprint_set,
                               'vulnerability_set': set_vulnerability_set,
                               'pla_loss_factors_set': set_loss_factors_set}

        for model_set, model_setter in optional_model_sets.items():
            model_set_val = self.settings.get('model_settings', {}).get(model_set)
            if model_set_val:
                model_setter(model_set_val, model_run_fp)

        # Test call to create fmpy files in GenerateLossesDir
        if il and self.fmpy:
            il_target_dir = os.path.join(self.model_run_dir, 'input')
            self.logger.info(f'Creating FMPY structures (IL): {il_target_dir}')
            create_financial_structure(self.ktools_alloc_rule_il, il_target_dir)

        if (ri or rl) and self.fmpy:
            for ri_sub_dir in ri_dirs:
                ri_target_dir = os.path.join(self.model_run_dir, 'input', ri_sub_dir)
                self.logger.info(f'Creating FMPY structures (RI): {ri_target_dir}')
                create_financial_structure(self.ktools_alloc_rule_ri, ri_target_dir)

        if self.summarypy:
            for runtype in [RUNTYPE_GROUNDUP_LOSS, RUNTYPE_INSURED_LOSS, RUNTYPE_REINSURANCE_LOSS]:
                if self.settings.get(f'{runtype}_output'):
                    summaries = self.settings.get('{}_summaries'.format(runtype), [])
                    summary_sets_id = np.sort([summary['id'] for summary in summaries if 'id' in summary])
                    if summary_sets_id.shape[0]:
                        if runtype == RUNTYPE_REINSURANCE_LOSS:
                            summary_dirs = [os.path.join(self.model_run_dir, 'input', ri_sub_dir) for ri_sub_dir in ri_dirs]
                        else:
                            summary_dirs = [os.path.join(self.model_run_dir, 'input')]
                        for summary_dir in summary_dirs:
                            self.logger.info(f'Creating summarypy structures {runtype}: {summary_dir}')
                            create_summary_object_file(summary_dir, runtype)

        self._store_run_settings(self.settings, os.path.join(model_run_fp, 'output'))


class GenerateLossesPartial(GenerateLossesDir):
    """
    Runs a single analysis event chunk
    """
    step_params = GenerateLossesDir.step_params + [
        {'name': 'ktools_num_processes', 'flag': '-n', 'type': int, 'default': KTOOLS_NUM_PROCESSES,
         'help': 'Number of ktools calculation processes to use'},
        {'name': 'ktools_event_shuffle', 'default': EVE_DEFAULT_SHUFFLE, 'type': int,
         'help': 'Set rule for event shuffling between eve partions, 0 - No shuffle, 1 - round robin (output elts sorted), 2 - Fisher-Yates shuffle, 3 - std::shuffle (previous default in oasislmf<1.14.0) '},
        {'name': 'ktools_alloc_rule_gul', 'default': KTOOLS_ALLOC_GUL_DEFAULT, 'type': int, 'help': 'Set the allocation used in gulcalc'},
        {'name': 'ktools_alloc_rule_il', 'default': KTOOLS_ALLOC_IL_DEFAULT, 'type': int,
         'help': 'Set the fmcalc allocation rule used in direct insured loss'},
        {'name': 'ktools_alloc_rule_ri', 'default': KTOOLS_ALLOC_RI_DEFAULT, 'type': int,
         'help': 'Set the fmcalc allocation rule used in reinsurance'},
        {'name': 'ktools_num_gul_per_lb', 'default': KTOOL_N_GUL_PER_LB, 'type': int,
         'help': 'Number of gul per load balancer (0 means no load balancer)'},
        {'name': 'ktools_num_fm_per_lb', 'default': KTOOL_N_FM_PER_LB, 'type': int,
         'help': 'Number of fm per load balancer (0 means no load balancer)'},
        {'name': 'ktools_disable_guard', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'Disables error handling in the ktools run script (abort on non-zero exitcode or output on stderr)'},
        {'name': 'ktools_fifo_relative', 'default': False, 'type': str2bool, 'const': True,
         'nargs': '?', 'help': 'Create ktools fifo queues under the ./fifo dir'},
        {'name': 'modelpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use getmodel python version instead of c++ version'},
        {'name': 'gulpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use gulcalc python version instead of c++ version'},
        {'name': 'gulpy_random_generator', 'default': 1, 'type': int,
         'help': 'set the random number generator in gulpy (0: Mersenne-Twister, 1: Latin Hypercube. Default: 1).'},
        {'name': 'gulmc', 'default': True, 'type': str2bool, 'const': True, 'nargs': '?', 'help': 'use full Monte Carlo gulcalc python version'},
        {'name': 'gulmc_random_generator', 'default': 1, 'type': int,
         'help': 'set the random number generator in gulmc (0: Mersenne-Twister, 1: Latin Hypercube. Default: 1).'},
        {'name': 'gulmc_effective_damageability', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use the effective damageability to draw loss samples instead of the full Monte Carlo method. Default: False'},
        {'name': 'gulmc_vuln_cache_size', 'default': 200, 'type': int,
         'help': 'Size in MB of the cache for the vulnerability calculations. Default: 200'},
        {'name': 'fmpy', 'default': True, 'type': str2bool, 'const': True, 'nargs': '?', 'help': 'use fmcalc python version instead of c++ version'},
        {'name': 'fmpy_low_memory', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use memory map instead of RAM to store loss array (may decrease performance but reduce RAM usage drastically)'},
        {'name': 'fmpy_sort_output', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?', 'help': 'order fmpy output by item_id'},
        {'name': 'model_custom_gulcalc', 'default': None, 'help': 'Custom gulcalc binary name to call in the model losses step'},
        {'name': 'peril_filter', 'default': [], 'nargs': '+', 'help': 'Peril specific run'},
        {'name': 'summarypy', 'default': False, 'type': str2bool, 'const': True,
            'nargs': '?', 'help': 'use summarycalc python version instead of c++ version'},
        {'name': 'join_summary_info', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'join summary id information to outputcalc csvs'},
        {'name': 'eltpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use eltpy python version instead of eltcalc c++ version'},
        {'name': 'pltpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use pltpy python version instead of pltcalc c++ version'},
        {'name': 'aalpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use aalpy python version instead of aalcalc c++ version'},
        {'name': 'lecpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use lecpy python version instead of ordleccalc c++ version'},
        {'name': 'base_df_engine', 'default': "oasis_data_manager.df_reader.reader.OasisPandasReader", 'help': 'The engine to use when loading dataframes'},
        {'name': 'exposure_df_engine', 'default': None,
            'help': 'The engine to use when loading dataframes exposure data (default: same as --base-df-engine)'},
        {'name': 'model_df_engine', 'default': None,
            'help': 'The engine to use when loading dataframes model data (default: same as --base-df-engine)'},
        {'name': 'dynamic_footprint', 'default': False,
            'help': 'Dynamic Footprint'},

        # New vars for chunked loss generation
        {'name': 'analysis_settings', 'default': None},
        {'name': 'script_fp', 'default': None},
        {'name': 'process_number', 'default': None, 'type': int, 'help': 'Partition number to run, if not set then run all in a single script'},
        {'name': 'max_process_id', 'default': -1, 'type': int, 'help': 'Max number of loss chunks, defaults to `ktools_num_processes` if not set'},
        {'name': 'ktools_fifo_queue_dir', 'default': None, 'is_path': True, 'help': 'Override the path used for fifo processing'},
    ]

    def run(self):
        GenerateLossesDir._check_ktool_rules(self)
        model_run_fp = GenerateLossesDir._get_output_dir(self)

        # distributed worker will pass in run settings as JSON, if not given load settings
        # and re-load input dir.
        if not self._is_run_settings_stored(os.path.join(model_run_fp, 'output')):
            GenerateLossesDir.run(self)

        ri_layers = self._get_num_ri_layers(self.settings, model_run_fp)
        model_runner_module, _ = self._get_model_runner()
        if not self.script_fp:
            script_name = 'run_analysis.sh' if not self.process_number else f'{self.process_number}.run_analysis.sh'
            self.script_fp = os.path.join(os.path.abspath(model_run_fp), script_name)

        if os.path.isfile(self.script_fp):
            os.remove(self.script_fp)

        bash_params = bash.bash_params(
            self.settings,
            number_of_processes=self.ktools_num_processes,
            filename=self.script_fp,
            num_reinsurance_iterations=ri_layers,
            gul_alloc_rule=self.ktools_alloc_rule_gul,
            il_alloc_rule=self.ktools_alloc_rule_il,
            ri_alloc_rule=self.ktools_alloc_rule_ri,
            num_gul_per_lb=self.ktools_num_gul_per_lb,
            num_fm_per_lb=self.ktools_num_fm_per_lb,
            bash_trace=self.verbose,
            stderr_guard=not self.ktools_disable_guard,
            gul_legacy_stream=self.ktools_legacy_stream,
            fifo_tmp_dir=not self.ktools_fifo_relative,
            custom_gulcalc_cmd=self.model_custom_gulcalc,
            gulpy=(self.gulpy and not self.model_custom_gulcalc),
            gulpy_random_generator=self.gulpy_random_generator,
            gulmc=(self.gulmc and not self.model_custom_gulcalc and not self.gulpy),
            gulmc_random_generator=self.gulmc_random_generator,
            gulmc_effective_damageability=self.gulmc_effective_damageability,
            gulmc_vuln_cache_size=self.gulmc_vuln_cache_size,
            fmpy=self.fmpy,
            fmpy_low_memory=self.fmpy_low_memory,
            fmpy_sort_output=self.fmpy_sort_output,
            event_shuffle=self.ktools_event_shuffle,
            process_number=self.process_number,
            max_process_id=self.max_process_id,
            modelpy=self.modelpy,
            peril_filter=self._get_peril_filter(self.settings),
            summarypy=self.summarypy,
            join_summary_info=self.join_summary_info,
            eltpy=self.eltpy,
            pltpy=self.pltpy,
            aalpy=self.aalpy,
            lecpy=self.lecpy,
            exposure_df_engine=self.exposure_df_engine or self.base_df_engine,
            model_df_engine=self.model_df_engine or self.base_df_engine,
            dynamic_footprint=self.dynamic_footprint
        )
        # Workaround test -- needs adding into bash_params
        if self.ktools_fifo_queue_dir:
            bash_params['fifo_queue_dir'] = self.ktools_fifo_queue_dir

        with setcwd(model_run_fp):
            try:
                if self.process_number:
                    self.logger.info('Generated loss Chunk {} of {} in, {}'.format(
                        bash_params['process_number'],
                        bash_params['max_process_id'],
                        model_run_fp,
                    ))
                else:
                    self.logger.info('All {} Loss chunks generated in {}'.format(bash_params['max_process_id'], model_run_fp))

                return model_runner_module.run_analysis(**bash_params)
            except CalledProcessError as e:
                log_fp = os.path.join(model_run_fp, 'log', str(bash_params.get('process_number', '')))
                self._print_error_logs(log_fp, e)

        return model_run_fp


class GenerateLossesOutput(GenerateLossesDir):
    """
    Runs the output reports generation on a set of event chunks
    """
    step_params = GenerateLossesDir.step_params + [
        {'name': 'analysis_settings_json', 'flag': '-a', 'is_path': True, 'pre_exist': True, 'required': True,
         'help': 'Analysis settings JSON file path'},
        {'name': 'ktools_num_processes', 'flag': '-n', 'type': int, 'default': KTOOLS_NUM_PROCESSES,
         'help': 'Number of ktools calculation processes to use'},
        {'name': 'ktools_disable_guard', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'Disables error handling in the ktools run script (abort on non-zero exitcode or output on stderr)'},
        {'name': 'ktools_fifo_relative', 'default': False, 'type': str2bool, 'const': True,
         'nargs': '?', 'help': 'Create ktools fifo queues under the ./fifo dir'},

        # New vars for chunked loss generation
        {'name': 'analysis_settings', 'default': None},
        {'name': 'script_fp', 'default': None},
        {'name': 'remove_working_file', 'default': False, 'help': 'Delete files in the "work/" dir onces outputs have completed'},
        {'name': 'max_process_id', 'default': -1, 'type': int, 'help': 'Max number of loss chunks, defaults to `ktools_num_processes` if not set'},
    ]

    def run(self):
        model_run_fp = GenerateLossesDir._get_output_dir(self)
        if not self._is_run_settings_stored(os.path.join(model_run_fp, 'output')):
            GenerateLossesDir.run(self)

        model_runner_module, _ = self._get_model_runner()
        ri_layers = self._get_num_ri_layers(self.settings, model_run_fp)

        if not self.script_fp:
            self.script_fp = os.path.join(os.path.abspath(model_run_fp), 'run_outputs.sh')

        if os.path.isfile(self.script_fp):
            os.remove(self.script_fp)

        bash_params = bash.bash_params(
            self.settings,
            number_of_processes=self.ktools_num_processes,
            num_reinsurance_iterations=ri_layers,
            filename=self.script_fp,
            bash_trace=self.verbose,
            stderr_guard=not self.ktools_disable_guard,
            fifo_tmp_dir=not self.ktools_fifo_relative,
            remove_working_file=self.remove_working_file,
            max_process_id=self.max_process_id,
        )
        with setcwd(model_run_fp):
            try:
                self.logger.info('Generating Loss outputs in {}'.format(model_run_fp))
                return model_runner_module.run_outputs(**bash_params)
            except CalledProcessError as e:
                log_fp = os.path.join(model_run_fp, 'log', 'out')
                self._print_error_logs(log_fp, e)
        return model_run_fp


class GenerateLosses(GenerateLossesDir):
    """
    Runs the GenerateLosses workflow as a single bash script (Default for the MDK)

    Generates losses using the installed ktools framework given Oasis files,
    model analysis settings JSON file, model data and model package data.

    The command line arguments can be supplied in the configuration file
    (``oasislmf.json`` by default or specified with the ``--config`` flag).
    Run ``oasislmf config --help`` for more information.

    The script creates a time-stamped folder in the model run directory and
    sets that as the new model run directory, copies the analysis settings
    JSON file into the run directory and creates the following folder
    structure
    ::

        |-- analysis_settings.json
        |-- fifo
        |-- input
            |-- RI_1
        |-- output
        |-- ri_layers.json
        |-- run_ktools.sh
        |-- static
        `-- work

    Depending on the OS type the model data is symlinked (Linux, Darwin) or
    copied (Cygwin, Windows) into the ``static`` subfolder. The input files
    are kept in the ``input`` subfolder and the losses are generated as CSV
    files in the ``output`` subfolder.
    """
    step_params = GenerateLossesDir.step_params + [
        {'name': 'ktools_num_processes', 'flag': '-n', 'type': int, 'default': KTOOLS_NUM_PROCESSES,
         'help': 'Number of ktools calculation processes to use'},
        {'name': 'ktools_event_shuffle', 'default': EVE_DEFAULT_SHUFFLE, 'type': int,
         'help': 'Set rule for event shuffling between eve partions, 0 - No shuffle, 1 - round robin (output elts sorted), 2 - Fisher-Yates shuffle, 3 - std::shuffle (previous default in oasislmf<1.14.0) '},
        {'name': 'ktools_alloc_rule_gul', 'default': KTOOLS_ALLOC_GUL_DEFAULT, 'type': int, 'help': 'Set the allocation used in gulcalc'},
        {'name': 'ktools_alloc_rule_il', 'default': KTOOLS_ALLOC_IL_DEFAULT, 'type': int,
         'help': 'Set the fmcalc allocation rule used in direct insured loss'},
        {'name': 'ktools_alloc_rule_ri', 'default': KTOOLS_ALLOC_RI_DEFAULT, 'type': int,
         'help': 'Set the fmcalc allocation rule used in reinsurance'},
        {'name': 'ktools_num_gul_per_lb', 'default': KTOOL_N_GUL_PER_LB, 'type': int,
         'help': 'Number of gul per load balancer (0 means no load balancer)'},
        {'name': 'ktools_num_fm_per_lb', 'default': KTOOL_N_FM_PER_LB, 'type': int,
         'help': 'Number of fm per load balancer (0 means no load balancer)'},
        {'name': 'ktools_disable_guard', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'Disables error handling in the ktools run script (abort on non-zero exitcode or output on stderr)'},
        {'name': 'ktools_fifo_relative', 'default': False, 'type': str2bool, 'const': True,
         'nargs': '?', 'help': 'Create ktools fifo queues under the ./fifo dir'},
        {'name': 'modelpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use getmodel python version instead of c++ version'},
        {'name': 'gulpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use gulcalc python version instead of c++ version'},
        {'name': 'gulpy_random_generator', 'default': 1, 'type': int,
         'help': 'set the random number generator in gulpy (0: Mersenne-Twister, 1: Latin Hypercube. Default: 1).'},
        {'name': 'gulmc', 'default': True, 'type': str2bool, 'const': True, 'nargs': '?', 'help': 'use full Monte Carlo gulcalc python version'},
        {'name': 'gulmc_random_generator', 'default': 1, 'type': int,
         'help': 'set the random number generator in gulmc (0: Mersenne-Twister, 1: Latin Hypercube. Default: 1).'},
        {'name': 'gulmc_effective_damageability', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use the effective damageability to draw loss samples instead of the full Monte Carlo method. Default: False'},
        {'name': 'gulmc_vuln_cache_size', 'default': 200, 'type': int,
         'help': 'Size in MB of the cache for the vulnerability calculations. Default: 200'},
        {'name': 'fmpy', 'default': True, 'type': str2bool, 'const': True, 'nargs': '?', 'help': 'use fmcalc python version instead of c++ version'},
        {'name': 'fmpy_low_memory', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
         'help': 'use memory map instead of RAM to store loss array (may decrease performance but reduce RAM usage drastically)'},
        {'name': 'fmpy_sort_output', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?', 'help': 'order fmpy output by item_id'},
        {'name': 'model_custom_gulcalc', 'default': None, 'help': 'Custom gulcalc binary name to call in the model losses step'},
        {'name': 'model_py_server', 'default': False, 'type': str2bool, 'help': 'running the data server for modelpy'},
        {'name': 'peril_filter', 'default': [], 'nargs': '+', 'help': 'Peril specific run'},
        {'name': 'summarypy', 'default': False, 'type': str2bool, 'const': True,
            'nargs': '?', 'help': 'use summarycalc python version instead of c++ version'},
        {'name': 'join_summary_info', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'join summary id information to outputcalc csvs'},
        {'name': 'eltpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use eltpy python version instead of eltcalc c++ version'},
        {'name': 'pltpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use pltpy python version instead of pltcalc c++ version'},
        {'name': 'aalpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use aalpy python version instead of aalcalc c++ version'},
        {'name': 'lecpy', 'default': False, 'type': str2bool, 'const': True, 'nargs': '?',
            'help': 'use lecpy python version instead of ordleccalc c++ version'},
        {'name': 'model_custom_gulcalc_log_start', 'default': None, 'help': 'Log message produced when custom gulcalc binary process starts'},
        {'name': 'model_custom_gulcalc_log_finish', 'default': None, 'help': 'Log message produced when custom gulcalc binary process ends'},
        {'name': 'base_df_engine', 'default': "oasis_data_manager.df_reader.reader.OasisPandasReader", 'help': 'The engine to use when loading dataframes'},
        {'name': 'model_df_engine', 'default': None,
            'help': 'The engine to use when loading model data dataframes (default: --base-df-engine if not set)'},
        {'name': 'exposure_df_engine', 'default': None,
            'help': 'The engine to use when loading exposure data dataframes (default: --base-df-engine if not set)'},
        {'name': 'dynamic_footprint', 'default': False,
            'help': 'Dynamic Footprint'},
    ]

    def run(self):
        # prep losses run dir / Setup
        GenerateLossesDir._check_ktool_rules(self)
        model_run_fp = GenerateLossesDir._get_output_dir(self)
        GenerateLossesDir.run(self)
        script_fp = os.path.join(os.path.abspath(model_run_fp), 'run_ktools.sh')
        ri_layers = self._get_num_ri_layers(self.settings, model_run_fp)
        model_runner_module, package_name = self._get_model_runner()

        with setcwd(model_run_fp):
            try:
                try:
                    run_args = dict(
                        number_of_processes=self.ktools_num_processes,
                        filename=script_fp,
                        num_reinsurance_iterations=ri_layers,
                        set_alloc_rule_gul=self.ktools_alloc_rule_gul,
                        set_alloc_rule_il=self.ktools_alloc_rule_il,
                        set_alloc_rule_ri=self.ktools_alloc_rule_ri,
                        num_gul_per_lb=self.ktools_num_gul_per_lb,
                        num_fm_per_lb=self.ktools_num_fm_per_lb,
                        run_debug=self.verbose,
                        stderr_guard=not self.ktools_disable_guard,
                        gul_legacy_stream=self.ktools_legacy_stream,
                        fifo_tmp_dir=not self.ktools_fifo_relative,
                        custom_gulcalc_cmd=self.model_custom_gulcalc,
                        custom_gulcalc_log_start=self.model_custom_gulcalc_log_start,
                        custom_gulcalc_log_finish=self.model_custom_gulcalc_log_finish,
                        gulpy=(self.gulpy and not self.model_custom_gulcalc),
                        gulpy_random_generator=self.gulpy_random_generator,
                        gulmc=(self.gulmc and not self.model_custom_gulcalc and not self.gulpy),
                        gulmc_random_generator=self.gulmc_random_generator,
                        gulmc_effective_damageability=self.gulmc_effective_damageability,
                        gulmc_vuln_cache_size=self.gulmc_vuln_cache_size,
                        fmpy=self.fmpy,
                        fmpy_low_memory=self.fmpy_low_memory,
                        fmpy_sort_output=self.fmpy_sort_output,
                        event_shuffle=self.ktools_event_shuffle,
                        modelpy=self.modelpy,
                        model_py_server=self.model_py_server,
                        peril_filter=self._get_peril_filter(self.settings),
                        summarypy=self.summarypy,
                        join_summary_info=self.join_summary_info,
                        eltpy=self.eltpy,
                        pltpy=self.pltpy,
                        aalpy=self.aalpy,
                        lecpy=self.lecpy,
                        model_df_engine=self.model_df_engine or self.base_df_engine,
                        dynamic_footprint=self.dynamic_footprint
                    )
                    model_runner_module.run(self.settings, **run_args)
                except TypeError:
                    warnings.simplefilter("always")
                    warnings.warn(
                        f"{package_name}.supplier_model_runner doesn't accept new runner arguments, please add **kwargs to the run function signature")
                    run_args = dict(
                        number_of_processes=self.ktools_num_processes,
                        filename=script_fp,
                        num_reinsurance_iterations=ri_layers,
                        set_alloc_rule_gul=self.ktools_alloc_rule_gul,
                        set_alloc_rule_il=self.ktools_alloc_rule_il,
                        set_alloc_rule_ri=self.ktools_alloc_rule_ri,
                        run_debug=self.verbose,
                        stderr_guard=not self.ktools_disable_guard,
                        gul_legacy_stream=self.ktools_legacy_stream,
                        fifo_tmp_dir=not self.ktools_fifo_relative,
                        custom_gulcalc_cmd=self.model_custom_gulcalc
                    )
                    model_runner_module.run(self.settings, **run_args)

            except CalledProcessError as e:
                bash_trace_fp = os.path.join(model_run_fp, 'log', 'bash.log')
                if os.path.isfile(bash_trace_fp):
                    with io.open(bash_trace_fp, 'r', encoding='utf-8') as f:
                        self.logger.info('\nBASH_TRACE:\n' + "".join(f.readlines()))

                stderror_fp = os.path.join(model_run_fp, 'log', 'stderror.err')
                if os.path.isfile(stderror_fp):
                    with io.open(stderror_fp, 'r', encoding='utf-8') as f:
                        self.logger.info('\nKTOOLS_STDERR:\n' + "".join(f.readlines()))

                gul_stderror_fp = os.path.join(model_run_fp, 'log', 'gul_stderror.err')
                if os.path.isfile(gul_stderror_fp):
                    with io.open(gul_stderror_fp, 'r', encoding='utf-8') as f:
                        self.logger.info('\nGUL_STDERR:\n' + "".join(f.readlines()))

                self.logger.info('\nSTDOUT:\n' + e.output.decode('utf-8').strip())

                if hasattr(model_runner_module, 'rerun'):
                    model_runner_module.rerun()

                raise OasisException(
                    'Ktools run Error: non-zero exit code or error/warning messages detected in STDERR output.\n'
                    'Killing all processes. To disable this automated check run with `--ktools-disable-guard`.\n'
                    'Logs stored in: {}/log'.format(model_run_fp)
                )

        self.logger.info('Losses generated in {}'.format(model_run_fp))
        return model_run_fp


class GenerateLossesDeterministic(ComputationStep):
    step_params = [
        {'name': 'oasis_files_dir', 'is_path': True, 'pre_exist': True},
        {'name': 'output_dir', 'default': None},
        {'name': 'include_loss_factor', 'default': True},
        {'name': 'loss_factor', 'default': [1.0]},
        {'name': 'net_ri', 'default': False},
        {'name': 'ktools_alloc_rule_il', 'default': KTOOLS_ALLOC_IL_DEFAULT},
        {'name': 'ktools_alloc_rule_ri', 'default': KTOOLS_ALLOC_RI_DEFAULT},
        {'name': 'fmpy', 'default': True},
        {'name': 'fmpy_low_memory', 'default': False},
        {'name': 'fmpy_sort_output', 'default': False},
        {'name': 'il_stream_type', 'default': 2},
    ]

    def run(self):

        losses = OrderedDict({'gul': None, 'il': None, 'ri': None})
        output_dir = self.output_dir or self.oasis_files_dir

        il = all(p in os.listdir(self.oasis_files_dir) for p in ['fm_policytc.csv', 'fm_profile.csv', 'fm_programme.csv', 'fm_xref.csv'])
        ri = any(re.match(r'RI_\d+$', fn) for fn in os.listdir(self.oasis_files_dir))

        step_flag = ''
        try:
            pd.read_csv(os.path.join(self.oasis_files_dir, 'fm_profile.csv'))['step_id']
        except (OSError, FileNotFoundError, KeyError):
            pass
        else:
            step_flag = '-S'

        csv_to_bin(self.oasis_files_dir, output_dir, il=il, ri=ri)

        # Generate an items and coverages dataframe and set column types (important!!)
        items = merge_dataframes(
            pd.read_csv(os.path.join(self.oasis_files_dir, 'items.csv')),
            pd.read_csv(os.path.join(self.oasis_files_dir, 'coverages.csv')),
            on=['coverage_id'], how='left'
        )

        dtypes = {t: ('uint32' if t != 'tiv' else 'float32') for t in items.columns}
        items = set_dataframe_column_dtypes(items, dtypes)
        items['count'] = items['coverage_id'].map(items['coverage_id'].value_counts())

        items['tiv'] = items['tiv'] / items['count']
        items.drop(columns=['count'], inplace=True)
        # Change order of stream depending on rule type
        #   Stream_type 1
        #     event_id, item_id, sidx, loss
        #     1,1,-1,0
        #     1,1,-2,0
        #     1,1,-3,10000
        #     1,1,1,10000
        #
        #   Stream_type 2
        #     event_id, item_id, sidx, loss
        #     1,1,-3,10000
        #     1,1,-2,0
        #     1,1,-1,0
        #     1,1,1,10000
        if self.il_stream_type == 2:
            gulcalc_sidxs = \
                [KTOOLS_TIV_SAMPLE_IDX, KTOOLS_STD_DEV_SAMPLE_IDX, KTOOLS_MEAN_SAMPLE_IDX] + \
                list(range(1, len(self.loss_factor) + 1))
        elif self.il_stream_type == 1:
            gulcalc_sidxs = \
                [KTOOLS_MEAN_SAMPLE_IDX, KTOOLS_STD_DEV_SAMPLE_IDX, KTOOLS_TIV_SAMPLE_IDX] + \
                list(range(1, len(self.loss_factor) + 1))
        else:
            OasisException("Unknown il stream type: {}".format(self.il_stream_type))

        # Set damage percentages corresponing to the special indexes.
        # We don't care about mean and std_dev, but
        # TIV needs to be set correctly.
        special_loss_factors = {
            KTOOLS_MEAN_SAMPLE_IDX: 0.,
            KTOOLS_STD_DEV_SAMPLE_IDX: 0.,
            KTOOLS_TIV_SAMPLE_IDX: 1.
        }

        loss_factor_map = {**special_loss_factors, **{i + 1: val for i, val in enumerate(self.loss_factor)}}

        guls = items[['item_id', 'tiv']].join(pd.DataFrame({'sidx': gulcalc_sidxs}, dtype='int64'), how='cross').assign(event_id=1)
        guls['loss'] = guls['sidx'].map(loss_factor_map) * guls['tiv']
        guls = guls.astype({
            'event_id': int,
            'item_id': int,
            'sidx': int,
            'loss': float})[['event_id', 'item_id', 'sidx', 'loss']]
        guls_fp = os.path.join(output_dir, "raw_guls.csv")
        guls.to_csv(guls_fp, index=False)

        # il_stream_type = 2 if self.fmpy else 1
        ils_fp = os.path.join(output_dir, 'raw_ils.csv')

        # Create IL fmpy financial structures
        if self.fmpy:
            with setcwd(self.oasis_files_dir):
                check_call(f"{get_fmcmd(self.fmpy)} -a {self.ktools_alloc_rule_il} --create-financial-structure-files -p {output_dir}", shell=True)

        cmd = 'gultobin -S {} -t {} < {} | {} -p {} -a {} {} | tee ils.bin | fmtocsv > {}'.format(
            len(self.loss_factor),
            self.il_stream_type,
            guls_fp,
            get_fmcmd(self.fmpy, self.fmpy_low_memory, self.fmpy_sort_output),
            output_dir,
            self.ktools_alloc_rule_il,
            step_flag, ils_fp
        )

        try:
            self.logger.debug("RUN: " + cmd)
            check_call(cmd, shell=True)
        except CalledProcessError as e:
            raise OasisException("Exception raised in 'generate_deterministic_losses'", e)

        guls.drop(guls[guls['sidx'] < 1].index, inplace=True)
        guls.reset_index(drop=True, inplace=True)
        if self.include_loss_factor:
            guls['loss_factor_idx'] = guls.apply(
                lambda r: int(r['sidx'] - 1), axis='columns')
        guls.drop('sidx', axis=1, inplace=True)
        guls = guls[(guls[['loss']] != 0).any(axis=1)]

        losses['gul'] = guls

        ils = get_dataframe(src_fp=ils_fp, lowercase_cols=False)
        ils.drop(ils[ils['sidx'] < 0].index, inplace=True)
        ils.reset_index(drop=True, inplace=True)
        if self.include_loss_factor:
            ils['loss_factor_idx'] = ils.apply(
                lambda r: int(r['sidx'] - 1), axis='columns')
        ils.drop('sidx', axis=1, inplace=True)
        ils = ils[(ils[['loss']] != 0).any(axis=1)]
        losses['il'] = ils

        if ri:
            try:
                [fn for fn in os.listdir(self.oasis_files_dir) if fn == 'ri_layers.json'][0]
            except IndexError:
                raise OasisException(
                    'No RI layers JSON file "ri_layers.json " found in the '
                    'input directory despite presence of RI input files'
                )
            else:
                try:
                    with io.open(os.path.join(self.oasis_files_dir, 'ri_layers.json'), 'r', encoding='utf-8') as f:
                        ri_layers = len(json.load(f))
                except (IOError, JSONDecodeError, OSError, TypeError) as e:
                    raise OasisException('Error trying to read the RI layers file: {}'.format(e))
                else:
                    def run_ri_layer(layer):
                        layer_inputs_fp = os.path.join(output_dir, 'RI_{}'.format(layer))
                        # Create RI fmpy financial structures
                        if self.fmpy:
                            with setcwd(self.oasis_files_dir):
                                check_call(
                                    f"{get_fmcmd(self.fmpy)} -a {self.ktools_alloc_rule_ri} --create-financial-structure-files -p {layer_inputs_fp}",
                                    shell=True)

                        _input = 'gultobin -S 1 -t {} < {} | {} -p {} -a {} {} | tee ils.bin |'.format(
                            self.il_stream_type,
                            guls_fp,
                            get_fmcmd(self.fmpy, self.fmpy_low_memory, self.fmpy_sort_output),
                            output_dir,
                            self.ktools_alloc_rule_il,
                            step_flag
                        ) if layer == 1 else ''
                        pipe_in_previous_layer = '< ri{}.bin'.format(layer - 1) if layer > 1 else ''
                        ri_layer_fp = os.path.join(output_dir, 'ri{}.csv'.format(layer))
                        net_flag = "-n" if self.net_ri else ""
                        cmd = '{} {} -p {} {} -a {} {} {} | tee ri{}.bin | fmtocsv > {}'.format(
                            _input,
                            get_fmcmd(self.fmpy, self.fmpy_low_memory, self.fmpy_sort_output),
                            layer_inputs_fp,
                            net_flag,
                            self.ktools_alloc_rule_ri,
                            pipe_in_previous_layer,
                            step_flag,
                            layer,
                            ri_layer_fp
                        )
                        try:
                            self.logger.debug("RUN: " + cmd)
                            check_call(cmd, shell=True)
                        except CalledProcessError as e:
                            raise OasisException("Exception raised in 'generate_deterministic_losses'", e)
                        rils = get_dataframe(src_fp=ri_layer_fp, lowercase_cols=False)
                        rils.drop(rils[rils['sidx'] < 0].index, inplace=True)
                        if self.include_loss_factor:
                            rils['loss_factor_idx'] = rils.apply(
                                lambda r: int(r['sidx'] - 1), axis='columns')

                        rils.drop('sidx', axis=1, inplace=True)
                        rils.reset_index(drop=True, inplace=True)
                        rils = rils[(rils[['loss']] != 0).any(axis=1)]

                        return rils

                    for i in range(1, ri_layers + 1):
                        rils = run_ri_layer(i)
                        if i in [1, ri_layers]:
                            losses['ri'] = rils

        return losses


class GenerateLossesDummyModel(GenerateDummyOasisFiles):
    settings_params = [{'name': 'analysis_settings_json', 'loader': analysis_settings_loader, 'user_role': 'user'}]

    step_params = [
        {'name': 'analysis_settings_json', 'flag': '-z', 'is_path': True, 'pre_exist': True, 'required': True,
         'help': 'Analysis settings JSON file path'},
        {'name': 'ktools_num_processes', 'flag': '-n', 'type': int, 'default': KTOOLS_NUM_PROCESSES,
         'required': False, 'help': 'Number of ktools calculation processes to use'},
        {'name': 'ktools_alloc_rule_gul', 'type': int, 'default': KTOOLS_ALLOC_GUL_DEFAULT,
         'required': False, 'help': 'Set the allocation rule used in gulcalc'},
        {'name': 'ktools_alloc_rule_il', 'type': int, 'default': KTOOLS_ALLOC_IL_DEFAULT,
         'required': False, 'help': 'Set the fmcalc allocation rule used in direct insured loss'}
    ]
    chained_commands = [GenerateDummyModelFiles, GenerateDummyOasisFiles]

    def _validate_input_arguments(self):
        super()._validate_input_arguments()
        alloc_ranges = {
            'ktools_alloc_rule_gul': KTOOLS_ALLOC_GUL_MAX,
            'ktools_alloc_rule_il': KTOOLS_ALLOC_FM_MAX
        }
        for rule in alloc_ranges:
            alloc_val = getattr(self, rule)
            if alloc_val < 0 or alloc_val > alloc_ranges[rule]:
                raise OasisException(f'Error: {rule}={alloc_val} - Not within valid range [0..{alloc_ranges[rule]}]')

    def _validate_analysis_settings(self):
        warnings.simplefilter('always')

        # RI output is unsupported
        if self.settings.get('ri_output'):
            warnings.warn('Generating reinsurance losses with dummy model not currently supported. Ignoring ri_output in analysis settings JSON.')
            self.settings['ri_output'] = False

        # No loc or acc files so grouping losses based on OED fields is
        # unsupported
        # No generation of return periods file so currently unsupported
        loss_types = [False, False]
        loss_params = [
            {
                'loss': 'GUL', 'output': 'gul_output',
                'summary': 'gul_summaries', 'num_summaries': 0
            }, {
                'loss': 'IL', 'output': 'il_output',
                'summary': 'il_summaries', 'num_summaries': 0
            }
        ]
        for idx, param in enumerate(loss_params):
            if self.settings.get(param['output']):
                param['num_summaries'] = len(self.settings[param['summary']])
                self.settings[param['summary']][:] = [x for x in self.settings[param['summary']] if not x.get('oed_fields')]
                num_dropped_summaries = param['num_summaries'] - len(self.settings[param['summary']])
                if num_dropped_summaries == param['num_summaries']:
                    warnings.warn(
                        f'Grouping losses based on OED fields is unsupported. No valid {param["loss"]} output. Please change {param["loss"]} settings in analysis settings JSON.')
                    self.settings[param['output']] = False
                elif num_dropped_summaries > 0:
                    warnings.warn(
                        f'Grouping losses based on OED fields is unsupported. {num_dropped_summaries} groups ignored in {param["loss"]} output.')
                if param['num_summaries'] > 1:  # Get first summary only
                    self.settings[param['summary']] = [self.settings[param['summary']][0]]
                if self.settings[param['output']]:
                    # We should only have one summary now
                    self.settings[param['summary']][0]['id'] = 1
                    if self.settings[param['summary']][0]['leccalc']['return_period_file']:
                        warnings.warn('Return period file is not generated. Please use "return_periods" field in analysis settings JSON.')
                        self.settings[param['summary']][0]['leccalc']['return_period_file'] = False
                    loss_types[idx] = True
        (self.gul, self.il) = loss_types

        # Check for valid outputs
        if not any([self.gul, self.il]):
            raise OasisException('No valid output settings. Please check analysis settings JSON.')
        if not self.gul:
            raise OasisException('Valid GUL output required. Please check analysis settings JSON.')

        # Determine whether random number file will exist
        if self.settings.get('model_settings').get('use_random_number_file'):
            if self.num_randoms == 0:
                warnings.warn('Ignoring use random number file option in analysis settings JSON as no random number file will be generated.')
                self.settings['model_settings']['use_random_number_file'] = False

    def _prepare_run_directory(self):
        super()._prepare_run_directory()
        self.output_dir = os.path.join(self.target_dir, 'output')
        self.work_dir = os.path.join(self.target_dir, 'work')
        directories = [
            self.output_dir, self.work_dir
        ]
        for directory in directories:
            if not os.path.exists(directory):
                Path(directory).mkdir(parents=True, exist_ok=True)

        # Write new analysis_settings.json to target directory
        analysis_settings_fp = os.path.join(
            self.target_dir, 'analysis_settings.json'
        )
        with open(analysis_settings_fp, 'w') as f:
            json.dump(self.settings, f, indent=4, ensure_ascii=False)

    def _write_summary_info_files(self):
        summary_info_df = pd.DataFrame(
            {'summary_id': [1], '_not_set_': ['All-Risks']}
        )
        summary_info_fp = [
            os.path.join(self.output_dir, 'gul_S1_summary-info.csv'),
            os.path.join(self.output_dir, 'il_S1_summary-info.csv')
        ]
        for fp, loss_type in zip(summary_info_fp, [self.gul, self.il]):
            if loss_type:
                summary_info_df.to_csv(
                    path_or_buf=fp, encoding='utf-8', index=False
                )

    def run(self):
        self.logger.info('\nProcessing arguments - Creating Model & Test Oasis Files')

        self._validate_input_arguments()
        self._validate_analysis_settings()
        self._create_target_directory(label='losses')
        self._prepare_run_directory()
        self._get_model_file_objects()
        self._get_gul_file_objects()

        self.il = False
        if self.settings.get('il_output'):
            self.il = True
            self._get_fm_file_objects()
        else:
            self.fm_files = []

        output_files = self.model_files + self.gul_files + self.fm_files
        for output_file in output_files:
            output_file.write_file()

        self.logger.info(f'\nGenerating losses (GUL=True, IL={self.il})')

        self._write_summary_info_files()
        if self.ktools_num_processes == KTOOLS_NUM_PROCESSES:
            self.ktools_num_processes = multiprocessing.cpu_count()
        script_fp = os.path.join(self.target_dir, 'run_ktools.sh')
        bash.genbash(
            max_process_id=self.ktools_num_processes,
            analysis_settings=self.settings,
            gul_alloc_rule=self.ktools_alloc_rule_gul,
            il_alloc_rule=self.ktools_alloc_rule_il,
            filename=script_fp
        )
        bash_trace = subprocess.check_output(['bash', script_fp])
        self.logger.info(bash_trace.decode('utf-8'))

        self.logger.info(f'\nDummy Model run completed successfully in {self.target_dir}')
