def is_sequence(obj):
    """
    Check if the object is a sequence of objects.
    String types are not included as sequences here.

    Parameters
    ----------
    obj : The object to check

    Returns
    -------
    is_sequence : bool
        Whether `obj` is a sequence of objects.

    Examples
    --------
    >>> l = [1, 2, 3]
    >>>
    >>> is_sequence(l)
    True
    >>> is_sequence(iter(l))
    False
    """

    if isinstance(obj, (str, bytes)):
        return False

    try:
        len(obj)  # Has a length associated with it.
        for item in obj:
            break
        else:
            return False  # obj is empty
        return True
    except TypeError:
        return False
