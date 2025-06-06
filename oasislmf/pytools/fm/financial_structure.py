__all__ = [
    'extract_financial_structure',
    'load_financial_structure',
    'create_financial_structure',
    'load_static',
]

import logging
import os

import numpy as np
from numba import from_dtype, njit, types
from numba.typed import Dict, List


from oasislmf.pytools.common.data import (load_as_ndarray, load_as_array, almost_equal,
                                          fm_policytc_dtype,
                                          fm_profile_csv_col_map, fm_profile_dtype, fm_profile_step_dtype,
                                          fm_programme_dtype,
                                          fm_xref_csv_col_map, fm_xref_dtype,
                                          items_dtype,
                                          oasis_int, nb_oasis_int, oasis_float, null_index)
from .common import (allowed_allocation_rule, need_extras, need_tiv_policy)

logger = logging.getLogger(__name__)

# temp dictionary types
node_type = types.UniTuple(nb_oasis_int, 2)
output_type = types.UniTuple(nb_oasis_int, 2)
layer_type = types.UniTuple(nb_oasis_int, 3)

# financial structure processed array
nodes_array_dtype = from_dtype(np.dtype([('node_id', np.uint64),
                                         ('level_id', oasis_int),
                                         ('agg_id', oasis_int),
                                         ('layer_len', oasis_int),
                                         ('cross_layer_profile', oasis_int),
                                         ('profile_len', oasis_int),
                                         ('profiles', oasis_int),
                                         ('loss', oasis_int),
                                         ('net_loss', oasis_int),
                                         ('extra', oasis_int),
                                         ('is_reallocating', np.uint8),
                                         ('parent_len', oasis_int),
                                         ('parent', oasis_int),
                                         ('children', oasis_int),
                                         ('output_ids', oasis_int),
                                         ]))

compute_info_dtype = from_dtype(np.dtype([('allocation_rule', oasis_int),
                                          ('max_level', oasis_int),
                                          ('max_layer', oasis_int),
                                          ('node_len', oasis_int),
                                          ('children_len', oasis_int),
                                          ('parents_len', oasis_int),
                                          ('profile_len', oasis_int),
                                          ('loss_len', oasis_int),
                                          ('extra_len', oasis_int),
                                          ('compute_len', oasis_int),
                                          ('start_level', oasis_int),
                                          ('items_len', oasis_int),
                                          ('output_len', oasis_int),
                                          ('stepped', np.bool_),
                                          ]))
profile_index_dtype = from_dtype(np.dtype([('i_start', oasis_int),
                                           ('i_end', oasis_int),
                                           ]))


def load_static(static_path):
    """
    Load the raw financial data from static_path as numpy ndarray
    first check if .bin file is present then try .cvs
    try loading profile_step before falling back to normal profile,

    :param static_path: str
            static_path
    :return:
        programme : link between nodes
        policytc : info on layer
        profile : policy profile can be profile_step or profile
        xref : node to output_id
        items : items (item_id and coverage_id mapping)
        coverages : Tiv value for each coverage id
    :raise:
        FileNotFoundError if one of the static is missing
    """
    programme = load_as_ndarray(static_path, 'fm_programme', fm_programme_dtype)
    policytc = load_as_ndarray(static_path, 'fm_policytc', fm_policytc_dtype)
    profile = load_as_ndarray(static_path, 'fm_profile_step', fm_profile_step_dtype, False, col_map=fm_profile_csv_col_map)
    if len(profile) == 0:
        profile = load_as_ndarray(static_path, 'fm_profile', fm_profile_dtype, col_map=fm_profile_csv_col_map)
        stepped = None
    else:
        stepped = True
    xref = load_as_ndarray(static_path, 'fm_xref', fm_xref_dtype, col_map=fm_xref_csv_col_map)

    items = load_as_ndarray(static_path, 'items', items_dtype, must_exist=False)[['item_id', 'coverage_id']]
    coverages = load_as_array(static_path, 'coverages', oasis_float, must_exist=False)
    if np.unique(items['coverage_id']).shape[0] != coverages.shape[0]:
        # one of the file is missing we default to empty array
        items = np.empty(0, dtype=items_dtype)
        coverages = np.empty(0, dtype=oasis_float)

    return programme, policytc, profile, stepped, xref, items, coverages


@njit(cache=True)
def does_nothing(profile):
    """
    evaluate if the profile is just doing nothing to the loss.
    this allows to save some memory and compulation time and memory during the calculation
    :param profile: np.array of fm_profile_dtype or fm_profile_step_dtype
            profile
    :return:
        boolean : True is profile is actually doing nothing
    """
    return ((profile['calcrule_id'] == 100) or
            (profile['calcrule_id'] == 12 and almost_equal(profile['deductible_1'], 0)) or
            (profile['calcrule_id'] == 15 and almost_equal(profile['limit_1'], 1)) or
            (profile['calcrule_id'] == 16 and almost_equal(profile['deductible_1'], 0)) or
            (profile['calcrule_id'] == 34 and almost_equal(profile['deductible_1'], 0)
                and almost_equal(profile['attachment_1'], 0)
                and almost_equal(profile['share_1'], 1))
            )


@njit(cache=True)
def get_all_children(node_to_dependencies, node, items_only):
    children = List()
    temp = List()
    temp.append(node)
    # children = []
    # temp = [node]

    while temp:
        parent = temp.pop()
        if parent in node_to_dependencies:
            if not items_only:
                children.append(parent)
            temp.extend(node_to_dependencies[parent])
        else:
            children.append(parent)

    return children


@njit(cache=True)
def get_all_parent(node_to_dependencies, node, max_level):
    res = set()
    temp = List()
    temp.extend(node)

    while temp:
        cur_node = temp.pop()
        if cur_node in node_to_dependencies:
            temp.extend(node_to_dependencies[cur_node])
            if cur_node[0] == max_level:
                res.add(cur_node)
        elif cur_node[0] <= max_level:
            res.add(cur_node)
    return List(res)


@njit(cache=True)
def is_multi_peril(fm_programme):
    for i in range(fm_programme.shape[0]):
        if fm_programme[i]['level_id'] == 1 and fm_programme[i]['from_agg_id'] != fm_programme[i]['to_agg_id']:
            return True
    else:
        return False


@njit(cache=True)
def get_tiv(children, items, coverages):
    used_cov = np.zeros_like(coverages, dtype=np.uint8)
    tiv = 0
    for child_programme in children:
        coverage_i = items[child_programme[1] - 1]['coverage_id'] - 1
        if not used_cov[coverage_i]:
            used_cov[coverage_i] = 1
            tiv += coverages[coverage_i]
    return tiv


@njit(cache=True)
def prepare_profile_simple(profile, tiv):
    # if use TIV convert calcrule to fix deductible
    if profile['calcrule_id'] == 4:
        profile['calcrule_id'] = 1
        profile['deductible_1'] *= tiv

    elif profile['calcrule_id'] == 6:
        profile['calcrule_id'] = 12
        profile['deductible_1'] *= tiv

    elif profile['calcrule_id'] == 18:
        profile['calcrule_id'] = 2
        profile['deductible_1'] *= tiv

    elif profile['calcrule_id'] == 21:
        profile['calcrule_id'] = 13
        profile['deductible_1'] *= tiv

    elif profile['calcrule_id'] == 9:
        profile['calcrule_id'] = 1
        profile['deductible_1'] *= profile['limit_1']
    elif profile['calcrule_id'] == 15:
        if profile['limit_1'] >= 1:
            profile['calcrule_id'] = 12


@njit(cache=True)
def prepare_profile_stepped(profile, tiv):
    # if use TIV convert calcrule to fix deductible
    if profile['calcrule_id'] == 27:
        profile['trigger_start'] *= tiv
        if profile['trigger_end'] == 1:
            profile['trigger_end'] = np.inf
        else:
            profile['trigger_end'] *= tiv
        loss = min(max(profile['payout_start'] * tiv - profile['deductible_1'], 0), profile['limit_1'])
        cond_loss = min(loss * profile['scale_2'], profile['limit_2'])
        profile['payout_start'] = (loss + cond_loss) * (1 + profile['scale_1'])

    elif profile['calcrule_id'] == 28:
        profile['trigger_start'] *= tiv
        if profile['trigger_end'] == 1:
            profile['trigger_end'] = np.inf
        else:
            profile['trigger_end'] *= tiv
        profile['scale_1'] += 1

        if profile['payout_start'] == 0:  # backward compatibility v1.22.x
            profile['calcrule_id'] = 281

    elif profile['calcrule_id'] == 29:
        profile['calcrule_id'] = 27
        profile['trigger_start'] *= tiv
        if profile['trigger_end'] == 1:
            profile['trigger_end'] = np.inf
        else:
            profile['trigger_end'] *= tiv
        loss = max(profile['payout_start'] * tiv - profile['deductible_1'], 0)
        cond_loss = min(loss * profile['scale_2'], profile['limit_2'])
        profile['payout_start'] = (loss + cond_loss) * (1 + profile['scale_1'])

    elif profile['calcrule_id'] == 30:
        profile['calcrule_id'] = 27
        profile['trigger_start'] *= tiv
        if profile['trigger_end'] == 1:
            profile['trigger_end'] = np.inf
        else:
            profile['trigger_end'] *= tiv
        loss = max(profile['payout_start'] * profile['limit_1'] - profile['deductible_1'], 0)
        cond_loss = min(loss * profile['scale_2'], profile['limit_2'])
        profile['payout_start'] = (loss + cond_loss) * (1 + profile['scale_1'])

    elif profile['calcrule_id'] == 31:
        profile['calcrule_id'] = 27
        profile['trigger_start'] *= tiv
        if profile['trigger_end'] == 1:
            profile['trigger_end'] = np.inf
        else:
            profile['trigger_end'] *= tiv
        loss = max(profile['payout_start'] - profile['deductible_1'], 0)
        cond_loss = min(loss * profile['scale_2'], profile['limit_2'])
        profile['payout_start'] = (loss + cond_loss) * (1 + profile['scale_1'])

    elif profile['calcrule_id'] == 32:
        profile['scale_1'] += 1

    elif profile['calcrule_id'] == 37:
        profile['trigger_start'] *= tiv
        if profile['trigger_end'] == 1:
            profile['trigger_end'] = np.inf
        else:
            profile['trigger_end'] *= tiv
        profile['scale_1'] += 1

    elif profile['calcrule_id'] == 38:
        profile['trigger_start'] *= tiv
        if profile['trigger_end'] == 1:
            profile['trigger_end'] = np.inf
        else:
            profile['trigger_end'] *= tiv
        profile['scale_1'] += 1

    else:
        prepare_profile_simple(profile, tiv)


@njit(cache=True)
def extract_financial_structure(allocation_rule, fm_programme, fm_policytc, fm_profile, stepped, fm_xref, items, coverages):
    """
    :param allocation_rule:
        option to indicate out the loss are allocated to the output
    :param fm_programme:
        structure of the levels
    :param fm_policytc:
        structure of the layers and policy_id to apply
    :param fm_profile:
        definition of the policy_id
    :param fm_xref:
        mapping between the output of the allocation and output item_id
    :return:
        compute_infos:
        nodes_array:
        node_parents_array:
        node_profiles_array:
        output_array:
    """
    ##### profile_id_to_profile_index ####
    # policies may have multiple step, crate a mapping between profile_id and the start and end index in fm_profile file
    max_profile_id = np.max(fm_profile['profile_id'])
    profile_id_to_profile_index = np.empty(max_profile_id + 1, dtype=profile_index_dtype)
    has_tiv_policy = Dict.empty(nb_oasis_int, nb_oasis_int)
    last_profile_id = 0  # real profile_id start at 1
    for i in range(fm_profile.shape[0]):
        if fm_profile[i]['calcrule_id'] in need_tiv_policy:
            has_tiv_policy[fm_profile[i]['profile_id']] = nb_oasis_int(0)
        profile_id_to_profile_index[fm_profile[i]['profile_id']]['i_end'] = i + 1
        if last_profile_id != fm_profile[i]['profile_id']:
            profile_id_to_profile_index[fm_profile[i]['profile_id']]['i_start'] = i
            last_profile_id = fm_profile[i]['profile_id']

    # in fm_programme check if multi-peril and get size of each levels
    max_level = np.max(fm_programme['level_id'])
    level_node_len = np.zeros(max_level + 1, dtype=oasis_int)
    multi_peril = False
    for i in range(fm_programme.shape[0]):
        programme = fm_programme[i]
        if programme['level_id'] == 1 and programme['from_agg_id'] != programme['to_agg_id']:
            multi_peril = True
        if level_node_len[programme['level_id'] - 1] < programme['from_agg_id']:
            level_node_len[programme['level_id'] - 1] = programme['from_agg_id']

        if level_node_len[programme['level_id']] < programme['to_agg_id']:
            level_node_len[programme['level_id']] = programme['to_agg_id']

    ##### fm_policytc (level_id agg_id layer_id => profile_id) #####
    # programme_node_to_profiles dict of (level_id, agg_id) => list of (layer_id, policy_index_start, policy_index_end)
    # for each policy needing tiv, we duplicate the policy for each node to then later on calculate the % tiv parameters
    programme_node_to_profiles = Dict.empty(node_type, List.empty_list(layer_type))
    programme_node_to_layers = Dict.empty(node_type, List.empty_list(layer_type))
    i_new_fm_profile = fm_profile.shape[0]
    new_fm_profile_list = List.empty_list(np.int64)
    for i in range(fm_policytc.shape[0]):
        policytc = fm_policytc[i]
        programme_node = (nb_oasis_int(policytc['level_id']), nb_oasis_int(policytc['agg_id']))
        i_start = profile_id_to_profile_index[nb_oasis_int(policytc['profile_id'])]['i_start']
        i_end = profile_id_to_profile_index[nb_oasis_int(policytc['profile_id'])]['i_end']

        if policytc['profile_id'] in has_tiv_policy:
            if has_tiv_policy[policytc['profile_id']]:
                for j in range(i_start, i_end):
                    new_fm_profile_list.append(j)
                i_start, i_end = i_new_fm_profile, i_new_fm_profile + i_end - i_start
                i_new_fm_profile = i_end
            else:
                has_tiv_policy[policytc['profile_id']] = nb_oasis_int(1)

        layer = (nb_oasis_int(policytc['layer_id']), nb_oasis_int(i_start), nb_oasis_int(i_end))

        if programme_node not in programme_node_to_profiles:
            _list = List.empty_list(layer_type)
            _list.append(layer)
            programme_node_to_profiles[programme_node] = _list
        else:
            programme_node_to_profiles[programme_node].append(layer)

    # create a new fm_profile with all the needed duplicated %tiv profiles
    if i_new_fm_profile - fm_profile.shape[0]:
        new_fm_profile = np.empty(i_new_fm_profile, dtype=fm_profile.dtype)
        new_fm_profile[:fm_profile.shape[0]] = fm_profile[:]
        for i in range(i_new_fm_profile - fm_profile.shape[0]):
            new_fm_profile[fm_profile.shape[0] + i] = fm_profile[new_fm_profile_list[i]]
        fm_profile = new_fm_profile

    # fm_xref
    if multi_peril:  # if single peril we can skip item level computation (level 0)
        start_level = nb_oasis_int(0)
    else:
        start_level = nb_oasis_int(1)

    if start_level == max_level:  # there is only one level we can switch the computation as if it were a0
        allocation_rule = 0

    if allocation_rule == 0:
        out_level = nb_oasis_int(max_level)
    else:
        out_level = start_level

    ##### xref #####
    # create mapping node (level_id, agg_id) => list of (layer_id, output_id)
    node_to_output_id = Dict.empty(node_type, Dict.empty(nb_oasis_int, nb_oasis_int))

    output_len = 0
    for i in range(fm_xref.shape[0]):
        xref = fm_xref[i]
        programme_node = (out_level, xref['agg_id'])
        if output_len < xref['output_id']:
            output_len = nb_oasis_int(xref['output_id'])

        if programme_node in node_to_output_id:
            node_to_output_id[programme_node][nb_oasis_int(xref['layer_id'])] = nb_oasis_int(xref['output_id'])
        else:
            _dict = Dict.empty(nb_oasis_int, nb_oasis_int)
            _dict[nb_oasis_int(xref['layer_id'])] = nb_oasis_int(xref['output_id'])
            node_to_output_id[programme_node] = _dict

    ##### programme ####
    # node_layers will contain the number of layer for each nodes
    node_layers = Dict.empty(node_type, nb_oasis_int)
    node_cross_layers = Dict.empty(node_type, nb_oasis_int)

    # fill up node_layers with the number of policies for each node
    for programme in fm_programme:
        parent = (nb_oasis_int(programme['level_id']), nb_oasis_int(programme['to_agg_id']))
        if parent not in node_layers:
            node_layers[parent] = nb_oasis_int(len(programme_node_to_profiles[parent]))
            programme_node_to_layers[parent] = programme_node_to_profiles[parent]

    # create 2 mapping to get the parents and the childs of each nodes
    # update the number of layer for nodes based on the number of layer of their parents
    # go through each level from top to botom
    parent_to_children = Dict.empty(node_type, List.empty_list(node_type))
    child_to_parents = Dict.empty(node_type, List.empty_list(node_type))

    children_len = 1
    parents_len = 0

    # go through each level from top to botom
    for level in range(max_level, start_level, -1):
        for programme in fm_programme:
            if programme['level_id'] == level:
                parent = (nb_oasis_int(programme['level_id']), nb_oasis_int(programme['to_agg_id']))

                if programme['from_agg_id'] > 0:  # level of node is programme['level_id'] - 1
                    child_programme = (nb_oasis_int(programme['level_id'] - 1), nb_oasis_int(programme['from_agg_id']))
                else:  # negative agg_id level is item level
                    child_programme = (start_level, nb_oasis_int(-programme['from_agg_id']))

                if parent not in parent_to_children:
                    children_len += 2
                    _list = List.empty_list(node_type)
                    _list.append(child_programme)
                    parent_to_children[parent] = _list
                    # parent_to_children[parent] = [child_programme]
                else:
                    children_len += 1
                    parent_to_children[parent].append(child_programme)

                parents_len += 1
                if child_programme not in child_to_parents:
                    _list = List.empty_list(node_type)
                    _list.append(parent)
                    child_to_parents[child_programme] = _list
                else:
                    child_to_parents[child_programme].insert(0, parent)
                # child_to_parents[child_programme] = [parent]
                if child_programme not in node_layers or node_layers[child_programme] <= node_layers[parent]:
                    node_layers[child_programme] = node_layers[parent]
                    programme_node_to_layers[child_programme] = programme_node_to_layers[parent]
                elif node_layers[child_programme] > node_layers[parent]:  # cross layer node
                    grand_parents = get_all_parent(child_to_parents, [parent], max_level)
                    for grand_parent in grand_parents:
                        if node_layers[grand_parent] < node_layers[child_programme]:
                            node_cross_layers[grand_parent] = nb_oasis_int(1)
                            node_layers[parent] = node_layers[child_programme]

    # compute number of steps (steps), max size of each level node_level_start, max size of node to compute (compute_len)
    node_level_start = np.zeros(level_node_len.shape[0] + 1, oasis_int)
    for i in range(start_level, level_node_len.shape[0]):
        node_level_start[i + 1] = node_level_start[i] + level_node_len[i]
    steps = max_level + (1 - start_level)
    compute_len = node_level_start[-1] + steps + level_node_len[-1] + 1

    output_array_size = 0
    for node, layer_size in node_layers.items():
        if node[0] == out_level:
            output_array_size += layer_size

    nodes_array = np.empty(node_level_start[-1] + 1, dtype=nodes_array_dtype)
    node_parents_array = np.empty(parents_len, dtype=oasis_int)
    node_profiles_array = np.zeros(fm_policytc.shape[0] + 1, dtype=profile_index_dtype)
    output_array = np.zeros(output_array_size, dtype=oasis_int)

    node_i = 1
    children_i = 1
    parents_i = 0
    profile_i = 1
    loss_i = 0
    extra_i = 0
    output_i = 0

    for level in range(start_level, max_level + 1):
        for agg_id in range(1, level_node_len[level] + 1):
            node_programme = (nb_oasis_int(level), nb_oasis_int(agg_id))
            node = nodes_array[node_i]
            node['node_id'] = node_i
            node_i += 1
            node['level_id'] = level
            node['agg_id'] = agg_id

            # layers
            node['layer_len'] = node_layers[node_programme]
            node['cross_layer_profile'] = 0  # set default to 0 change if it is a cross_layer_profile after
            node['loss'], loss_i = loss_i, loss_i + node['layer_len']
            if level == start_level:
                node['net_loss'], loss_i = loss_i, loss_i + 1

            node['extra'] = null_index
            node['is_reallocating'] = 0

            # children
            if node_programme in parent_to_children:
                children = parent_to_children[node_programme]
                node['children'], children_i = children_i, children_i + 1 + len(children)
            else:
                node['children'] = 0

            # parent
            if node_programme in child_to_parents:
                parents = child_to_parents[node_programme]
                node['parent_len'] = len(parents)
                node['parent'] = parents_i
                for parent in parents:
                    node_parents_array[parents_i], parents_i = node_level_start[parent[0]] + parent[1], nb_oasis_int(parents_i + 1)
            else:
                node['parent_len'] = 0

            # profiles
            if node_programme in programme_node_to_profiles:
                profiles = programme_node_to_profiles[node_programme]
                if node_programme in node_cross_layers:
                    node['profile_len'] = node['layer_len']
                    node['cross_layer_profile'] = 1
                else:
                    node['profile_len'] = len(profiles)
                node['profiles'] = profile_i

                for layer_id, i_start, i_end in sorted(profiles):
                    node_profile, profile_i = node_profiles_array[profile_i], profile_i + 1
                    node_profile['i_start'] = i_start
                    node_profile['i_end'] = i_end

                    # if use TIV we compute it and precompute % TIV values
                    for profile_index in range(i_start, i_end):
                        if fm_profile[profile_index]['calcrule_id'] in need_tiv_policy:
                            all_children = get_all_children(parent_to_children, node_programme, True)
                            tiv = get_tiv(all_children, items, coverages)
                            break
                    else:
                        tiv = 0

                    for profile_index in range(i_start, i_end):
                        profile = fm_profile[profile_index]
                        if stepped is None:
                            prepare_profile_simple(profile, tiv)
                        else:
                            prepare_profile_stepped(profile, tiv)
                        if does_nothing(profile):
                            # only non step policy can "does_nothing" so this is safe
                            node_profile['i_end'] = node_profile['i_start']

                    # check if we need to compute extras (min and max ded policies)
                    for profile_index in range(i_start, i_end):
                        if fm_profile[profile_index]['calcrule_id'] in need_extras:
                            node['is_reallocating'] = allocation_rule == 2 and fm_profile[profile_index]['calcrule_id'] != 27

                            items_child = get_all_children(parent_to_children, node_programme, True)
                            all_parent = get_all_parent(child_to_parents, items_child, node_programme[0])

                            for parent in all_parent:
                                all_children = get_all_children(parent_to_children, parent, False)
                                for child_programme in all_children:  # include current node
                                    child = nodes_array[node_level_start[child_programme[0]] + child_programme[1]]
                                    if child['extra'] == null_index:
                                        child['extra'], extra_i = extra_i, extra_i + node['layer_len']

                            break

            else:  # item level has no profile
                node['profile_len'] = 1
                node['profiles'] = 0

            if level == out_level:
                if node_programme in node_to_output_id:
                    node['output_ids'], output_i = output_i, output_i + node['layer_len']
                    for i, (layer_id, _, _) in enumerate(programme_node_to_layers[node_programme]):
                        if layer_id in node_to_output_id[node_programme]:
                            output_array[node['output_ids'] + i] = node_to_output_id[node_programme][layer_id]
                else:
                    raise KeyError("Some output nodes are missing output_ids")

    compute_infos = np.empty(1, dtype=compute_info_dtype)
    compute_info = compute_infos[0]
    compute_info['allocation_rule'] = allocation_rule
    compute_info['max_level'] = max_level
    compute_info['node_len'] = node_i
    compute_info['children_len'] = children_i
    compute_info['parents_len'] = parents_i
    compute_info['profile_len'] = profile_i
    compute_info['loss_len'] = loss_i
    compute_info['extra_len'] = extra_i
    compute_info['compute_len'] = compute_len
    compute_info['start_level'] = start_level
    compute_info['items_len'] = level_node_len[0]
    compute_info['output_len'] = output_len
    compute_info['stepped'] = stepped is not None
    compute_info['max_layer'] = max(nodes_array['layer_len'][1:])

    return compute_infos, nodes_array, node_parents_array, node_profiles_array, output_array, fm_profile


def create_financial_structure(allocation_rule, static_path):
    """
    :param allocation_rule: int
            back-allocation rule
    :param static_path: string
            path to the static files
    :return:
        compute_queue : the step of the computation to perform on each event
        node_indexes : map node to index of item in result array
        index_dependencies : map node to its dependent indexes
        node_profile : map node to profile
        output_item_index : list of item_id, index to put in the output
    """

    if allocation_rule not in allowed_allocation_rule:
        raise ValueError(f"allocation_rule must be in {allowed_allocation_rule}, found {allocation_rule}")
    if allocation_rule == 3:
        allocation_rule = 2

    fm_programme, fm_policytc, fm_profile, stepped, fm_xref, items, coverages = load_static(static_path)
    financial_structure = extract_financial_structure(allocation_rule, fm_programme, fm_policytc, fm_profile,
                                                      stepped, fm_xref, items, coverages)
    compute_info, nodes_array, node_parents_array, node_profiles_array, output_array, fm_profile = financial_structure
    logger.info(f'nodes_array has {len(nodes_array)} elements')
    logger.info(f'compute_info : {dict(zip(compute_info.dtype.names, compute_info[0]))}')

    np.save(os.path.join(static_path, f'compute_info_{allocation_rule}'), compute_info)
    np.save(os.path.join(static_path, f'nodes_array_{allocation_rule}'), nodes_array)
    np.save(os.path.join(static_path, f'node_parents_array_{allocation_rule}'), node_parents_array)
    np.save(os.path.join(static_path, f'node_profiles_array_{allocation_rule}'), node_profiles_array)
    np.save(os.path.join(static_path, f'output_array_{allocation_rule}'), output_array)
    np.save(os.path.join(static_path, 'fm_profile'), fm_profile)


def load_financial_structure(allocation_rule, static_path):
    compute_info = np.load(os.path.join(static_path, f'compute_info_{allocation_rule}.npy'), mmap_mode='r')
    nodes_array = np.load(os.path.join(static_path, f'nodes_array_{allocation_rule}.npy'), mmap_mode='r')
    node_parents_array = np.load(os.path.join(static_path, f'node_parents_array_{allocation_rule}.npy'), mmap_mode='r')
    node_profiles_array = np.load(os.path.join(static_path, f'node_profiles_array_{allocation_rule}.npy'), mmap_mode='r')
    output_array = np.load(os.path.join(static_path, f'output_array_{allocation_rule}.npy'), mmap_mode='r')
    fm_profile = np.load(os.path.join(static_path, 'fm_profile.npy'), mmap_mode='r')

    return compute_info, nodes_array, node_parents_array, node_profiles_array, output_array, fm_profile
