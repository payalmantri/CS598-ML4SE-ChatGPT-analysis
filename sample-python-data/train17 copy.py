def _create_converter(dataType):
    """Create a converter to drop the names of fields in obj """
    def converter_helper(dataType):
        if not _need_converter(dataType):
            return lambda x: x

        elif isinstance(dataType, ArrayType):
            conv = converter_helper(dataType.elementType)
            return lambda row: [conv(v) for v in row]

        elif isinstance(dataType, MapType):
            kconv = converter_helper(dataType.keyType)
            vconv = converter_helper(dataType.valueType)
            return lambda row: dict((kconv(k), vconv(v)) for k, v in row.items())

        elif isinstance(dataType, NullType):
            return lambda x: None

        elif not isinstance(dataType, StructType):
            return lambda x: x

        # dataType must be StructType
        names = [f.name for f in dataType.fields]
        converters = [converter_helper(f.dataType) for f in dataType.fields]
        convert_fields = any(_need_converter(f.dataType) for f in dataType.fields)

        def convert_struct(obj):
            if obj is None:
                return

            if isinstance(obj, (tuple, list)):
                if convert_fields:
                    return tuple(conv(v) for v, conv in zip(obj, converters))
                else:
                    return tuple(obj)

            if isinstance(obj, dict):
                d = obj
            elif hasattr(obj, "__dict__"):  # object
                d = obj.__dict__
            else:
                raise TypeError("Unexpected obj type: %s" % type(obj))

            if convert_fields:
                return tuple([conv(d.get(name)) for name, conv in zip(names, converters)])
            else:
                return tuple([d.get(name) for name in names])

        return convert_struct
    
    return converter_helper(dataType)
