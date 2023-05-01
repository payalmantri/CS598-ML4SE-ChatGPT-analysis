def _int_size_to_type(size):
    """
    Return the Catalyst datatype from the size of integers.
    """
    type_size_dict = {
        8: ByteType,
        16: ShortType,
        32: IntegerType,
        64: LongType
    }
    for int_size in sorted(type_size_dict.keys()):
        if size <= int_size:
            return type_size_dict[int_size]
    return LongType  # fallback option if size > 64
