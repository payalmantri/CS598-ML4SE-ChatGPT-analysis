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

    return (isinstance(obj, abc.Iterable) and
            # we do not count strings/unicode/bytes as list-like
            not isinstance(obj, (str, bytes)) and

            # exclude zero-dimensional numpy arrays, effectively scalars
            not (isinstance(obj, np.ndarray) and obj.ndim == 0) and

            # exclude sets if allow_sets is False
            not (allow_sets is False and isinstance(obj, abc.Set)))