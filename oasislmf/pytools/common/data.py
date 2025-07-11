import os
import numba as nb
import numpy as np
import pandas as pd


oasis_int = np.dtype(os.environ.get('OASIS_INT', 'i4'))
nb_oasis_int = nb.from_dtype(oasis_int)
oasis_int_size = oasis_int.itemsize

oasis_float = np.dtype(os.environ.get('OASIS_FLOAT', 'f4'))
nb_oasis_float = nb.from_dtype(oasis_float)
oasis_float_size = oasis_float.itemsize

areaperil_int = np.dtype(os.environ.get('AREAPERIL_TYPE', 'u4'))
nb_areaperil_int = nb.from_dtype(areaperil_int)
areaperil_int_size = areaperil_int.itemsize

null_index = oasis_int.type(-1)


summary_xref_dtype = np.dtype([('item_id', 'i4'), ('summary_id', 'i4'), ('summary_set_id', 'i4')])


# financial structure static input dtypes
fm_programme_dtype = np.dtype([('from_agg_id', 'i4'), ('level_id', 'i4'), ('to_agg_id', 'i4')])
fm_policytc_dtype = np.dtype([('level_id', 'i4'), ('agg_id', 'i4'), ('layer_id', 'i4'), ('profile_id', 'i4')])
fm_profile_dtype = np.dtype([('profile_id', 'i4'),
                             ('calcrule_id', 'i4'),
                             ('deductible_1', oasis_float),
                             ('deductible_2', oasis_float),
                             ('deductible_3', oasis_float),
                             ('attachment_1', oasis_float),
                             ('limit_1', oasis_float),
                             ('share_1', oasis_float),
                             ('share_2', oasis_float),
                             ('share_3', oasis_float),
                             ])
fm_profile_step_dtype = np.dtype([('profile_id', 'i4'),
                                  ('calcrule_id', 'i4'),
                                  ('deductible_1', oasis_float),
                                  ('deductible_2', oasis_float),
                                  ('deductible_3', oasis_float),
                                  ('attachment_1', oasis_float),
                                  ('limit_1', oasis_float),
                                  ('share_1', oasis_float),
                                  ('share_2', oasis_float),
                                  ('share_3', oasis_float),
                                  ('step_id', 'i4'),
                                  ('trigger_start', oasis_float),
                                  ('trigger_end', oasis_float),
                                  ('payout_start', oasis_float),
                                  ('payout_end', oasis_float),
                                  ('limit_2', oasis_float),
                                  ('scale_1', oasis_float),
                                  ('scale_2', oasis_float),
                                  ])
fm_profile_csv_col_map = {
    'deductible_1': 'deductible1',
    'deductible_2': 'deductible2',
    'deductible_3': 'deductible3',
    'attachment_1': 'attachment1',
    'limit_1': 'limit1',
    'share_1': 'share1',
    'share_2': 'share2',
    'share_3': 'share3',
    'limit_2': ' limit2',
    'scale_1': 'scale1',
    'scale_2': 'scale2',
}
fm_xref_dtype = np.dtype([('output_id', 'i4'), ('agg_id', 'i4'), ('layer_id', 'i4')])
fm_xref_csv_col_map = {'output_id': 'output'}

# seemingly unused but coverage TIV in ktools typically defined as OASIS_FLOAT
coverages_dtype = np.dtype([('coverage_id', 'i4'), ('tiv', oasis_float)])

items_dtype = np.dtype([('item_id', 'i4'),
                        ('coverage_id', 'i4'),
                        ('areaperil_id', areaperil_int),
                        ('vulnerability_id', 'i4'),
                        ('group_id', 'i4')])

# Mean type numbers for outputs (SampleType)
MEAN_TYPE_ANALYTICAL = 1
MEAN_TYPE_SAMPLE = 2


def load_as_ndarray(dir_path, name, _dtype, must_exist=True, col_map=None):
    """
    load a file as a numpy ndarray
    useful for multi-columns files
    Args:
        dir_path: path to the directory where the binary or csv file is stored
        name: name of the file
        _dtype: np.dtype
        must_exist: raise FileNotFoundError if no file is present
        col_map: name re-mapping to change name of csv columns
    Returns:
        numpy ndarray
    """

    if os.path.isfile(os.path.join(dir_path, name + '.bin')):
        return np.fromfile(os.path.join(dir_path, name + '.bin'), dtype=_dtype)
    elif must_exist or os.path.isfile(os.path.join(dir_path, name + '.csv')):
        # in csv column cam be out of order and have different name,
        # we load with pandas and write each column to the ndarray
        if col_map is None:
            col_map = {}
        with open(os.path.join(dir_path, name + '.csv')) as file_in:
            cvs_dtype = {col_map.get(key, key): col_dtype for key, (col_dtype, _) in _dtype.fields.items()}
            df = pd.read_csv(file_in, delimiter=',', dtype=cvs_dtype, usecols=list(cvs_dtype.keys()))
            res = np.empty(df.shape[0], dtype=_dtype)
            for name in _dtype.names:
                res[name] = df[col_map.get(name, name)]
            return res
    else:
        return np.empty(0, dtype=_dtype)


def load_as_array(dir_path, name, _dtype, must_exist=True):
    """
    load file as a single numpy array,
     useful for files with a binary version with only one type of value where their index correspond to an id.
     For example coverage.bin only contains tiv value for each coverage id
     coverage_id n correspond to index n-1
    Args:
        dir_path: path to the directory where the binary or csv file is stored
        name: name of the file
        _dtype: numpy dtype of the required array
        must_exist: raise FileNotFoundError if no file is present
    Returns:
        numpy array of dtype type
    """
    fp = os.path.join(dir_path, name + '.bin')
    if os.path.isfile(fp):
        return np.fromfile(fp, dtype=_dtype)
    elif must_exist or os.path.isfile(os.path.join(dir_path, name + '.csv')):
        fp = os.path.join(dir_path, name + '.csv')
        with open(fp) as file_in:
            return np.loadtxt(file_in, dtype=_dtype, delimiter=',', skiprows=1, usecols=1)
    else:
        return np.empty(0, dtype=_dtype)


def write_ndarray_to_fmt_csv(output_file, data, headers, row_fmt):
    """Writes a custom dtype array with headers to csv with the provided row_fmt str

    This function is a faster replacement for np.savetxt as it formats each row one at a time before writing to csv.
    We create one large string, and formats all the data at once, and writes all the data at once.

    WARNING: untested with string types in custom data.

    Args:
        output_file (io.TextIOWrapper): CSV file
        data (ndarray[<custom dtype>]): Custom dtype ndarray with column names
        headers (list[str]): Column names for custom ndarray
        row_fmt (str): Format for each row in csv
    """
    if len(headers) != len(row_fmt.split(",")):
        raise RuntimeError(f"ERROR: write_ndarray_to_fmt_csv requires row_fmt ({row_fmt}) and headers ({headers}) to have the same length.")

    # Copy data as np.ravel does not work with custom dtype arrays
    # Default type of np.empty is np.float64.
    data_cpy = np.empty((data.shape[0], len(headers)))
    for i in range(len(headers)):
        data_cpy[:, i] = data[headers[i]]

    # Create one large formatted string
    final_fmt = "\n".join([row_fmt] * data_cpy.shape[0])
    str_data = final_fmt % tuple(np.ravel(data_cpy))

    output_file.write(str_data)
    output_file.write("\n")


float_equal_precision = np.finfo(oasis_float).eps


@nb.njit(cache=True)
def almost_equal(a, b):
    return abs(a - b) < float_equal_precision
