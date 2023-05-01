def construct_1d_arraylike_from_scalar(value, length, dtype):
    """
    create a np.ndarray / pandas type of specified shape and dtype
    filled with values

    Parameters
    ----------
    value : scalar value
    length : int
    dtype : pandas_dtype / np.dtype

    Returns
    -------
    np.ndarray / pandas type of length, filled with value

    """
    if is_datetime64tz_dtype(dtype):
        from pandas import DatetimeIndex
        subarr = DatetimeIndex([value] * length, dtype=dtype)
    elif is_categorical_dtype(dtype):
        from pandas import Categorical
        subarr = Categorical([value] * length, dtype=dtype)
    else:
        if not isinstance(dtype, (np.dtype, type(np.dtype))):
            dtype = dtype.dtype

        if isna(value):
            if is_integer_dtype(dtype):
                value = np.nan
                dtype = np.dtype('float64')
            elif isinstance(dtype, np.dtype) and dtype.kind in ("U", "S"):
                dtype = object
                value = to_str(value)
            else:
                raise ValueError(f"cannot fill array of type {dtype} with NA")

        subarr = np.full(length, value, dtype=dtype)

    return subarr
