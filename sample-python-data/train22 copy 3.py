def maybe_convert_platform_interval(values):
    """
    Try to do platform conversion, with special casing for IntervalArray.
    Wrapper around maybe_convert_platform that alters the default return
    dtype in certain cases to be compatible with IntervalArray.  For example,
    empty lists return with integer dtype instead of object dtype, which is
    prohibited for IntervalArray.

    Parameters
    ----------
    values : array-like

    Returns
    -------
    array
    """
    if isinstance(values, (list, tuple)) and len(values) > 0:
        # GH 19016
        # empty lists/tuples get object dtype by default, but this is not
        # prohibited for IntervalArray, so coerce to integer instead
        return np.array([], dtype=np.int64)
    elif is_categorical_dtype(values):
        values = np.asarray(values)

    return maybe_convert_platform(values)