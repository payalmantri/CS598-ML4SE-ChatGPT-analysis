def is_list_like(obj, allow_sets=True):
    """
    Check if the object is list-like.

    Objects that are considered list-like are for example Python
    lists, tuples, sets, NumPy arrays, and Pandas Series.

    Strings and datetime objects, however, are not considered list-like.

    Parameters
    ----------
    obj : The object to check
    allow_sets : boolean, default True
        If this parameter is False, sets will not be considered list-like

        .. versionadded:: 0.24.0

    Returns
    -------
    is_list_like : bool
        Whether `obj` has list-like properties.

    Examples
    --------
    >>> is_list_like([1, 2, 3])
    True
    >>> is_list_like({1, 2, 3})
    True
    >>> is_list_like(datetime(2017, 1, 1))
    False
    >>> is_list_like("foo")
    False
    >>> is_list_like(1)
    False
    >>> is_list_like(np.array([2]))
    True
    >>> is_list_like(np.array(2)))
    False
    """

    if not isinstance(obj, abc.Iterable):
        return False

    if isinstance(obj, (str, bytes)):
        return False

    if isinstance(obj, np.ndarray) and obj.ndim == 0:
        return False

    if allow_sets is False and isinstance(obj, abc.Set):
        return False

    return True
