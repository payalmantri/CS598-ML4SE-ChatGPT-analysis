def _has_nulltype(dt):
    """ Return whether there is NullType in `dt` or not """
    def has_nulltype_helper(dt):
        if isinstance(dt, StructType):
            for f in dt.fields:
                if has_nulltype_helper(f.dataType):
                    return True
        elif isinstance(dt, ArrayType):
            return has_nulltype_helper(dt.elementType)
        elif isinstance(dt, MapType):
            return has_nulltype_helper(dt.keyType) or has_nulltype_helper(dt.valueType)
        else:
            return isinstance(dt, NullType)
    
    return has_nulltype_helper(dt)
