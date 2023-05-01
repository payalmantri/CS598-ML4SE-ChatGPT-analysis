def is_file_like(obj):
    """
    Check if the object is a file-like object.

    For objects to be considered file-like, they must
    have a `read` and/or `write` method as an attribute.

    Note: file-like objects must be iterable, but
    iterable objects need not be file-like.

    .. versionadded:: 0.20.0

    Parameters
    ----------
    obj : The object to check

    Returns
    -------
    is_file_like : bool
        Whether `obj` has file-like properties.

    Examples
    --------
    >>> buffer(StringIO("data"))
    >>> is_file_like(buffer)
    True
    >>> is_file_like([1, 2, 3])
    False
    """

    return hasattr(obj, 'read') or hasattr(obj, 'write')
