def cast_scalar_to_array(shape, value, dtype=None):
    """
    create np.ndarray of specified shape and dtype, filled with values

    Parameters
    ----------
    shape : tuple
    value : scalar value
    dtype : np.dtype, optional
        dtype to coerce

    Returns
    -------
    ndarray of shape, filled with value, of specified / inferred dtype

    """
    if dtype is None:
        dtype, fill_value = infer_dtype_from_scalar(value)
    else:
        fill_value = value

    if isinstance(shape, int):
        shape = (shape,)

    arr_shape = np.zeros(len(shape), dtype=np.intp)
    for i, dim in enumerate(shape):
        arr_shape[i] = dim

    values = np.empty(arr_shape, dtype=dtype)
    values.fill(fill_value)

    return values
