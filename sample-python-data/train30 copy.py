def construct_1d_object_array_from_listlike(values):
    """
    Transform any list-like object in a 1-dimensional numpy array of object
    dtype.

    Parameters
    ----------
    values : any iterable which has a len()

    Raises
    ------
    TypeError
        * If `values` does not have a len()

    Returns
    -------
    1-dimensional numpy array of dtype object
    """
    try:
        length = len(values)
    except TypeError:
        raise TypeError(f"'{type(values).__name__}' object is not iterable")

    result = np.fromiter(values, dtype='object', count=length)
    return result
