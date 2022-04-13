
def union(dict_1, dict_2):
    """
    Finding the union of given two dictionaries
    py:function::

    Args:
        dict_1,dict_2 (dict): dictionaries to find union

    Returns:
        dict: dictionary of union of given dictionaries.
    """
    ret = {}
    for x in dict_1:
        ret[x] = 1
    for y in dict_2:
        if y not in ret:
            ret[y] = 1
    return ret


def intersection(dict_1, dict_2):
    """
    Finding the intersection of given two dictionaries
    py:function::

    Args:
        dict_1,dict_2 (dict): dictionaries to find intersection

    Returns:
        dict: dictionary of intersection of given dictionaries.
    """
    duplicate_dict = {}
    for x in dict_1:
        if x in dict_2:
            duplicate_dict[x] = 1
    return duplicate_dict


def minus(dict_1, dict_2):
    """
    Finding minus of given two dictionaries
    py:function::

    Args:
        dict_1,dict_2 (dict): dictionaries to find minus

    Returns:
        dict: dictionary of minus of given dictionaries.
    """
    duplicate_dict = {}
    for x in dict_1:
        if x not in dict_2:
            duplicate_dict[x] = 1
    return duplicate_dict
