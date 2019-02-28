class Domain:
    parameters_order = None  # list of names of domain parameters, will be useful when RAM->XML
    name = None
    type = None
    align = None
    width = None
    char_length = None
    description = None
    props = None  # set of props
    precision = None
    scale = None
    length = None

    unnamed = None
    position_for_unnamed = None  # list of 2 elements: 0 - table name, 1 - field name

    def __init__(self, name, type, unnamed):
        self.unnamed = unnamed
        self.parameters_order = []
        if (name is not None) & (name != ""):
            self.name = name.replace(" ", "_").\
                replace("\\", "_")\
                .replace("-", "_").\
                replace(".", "").\
                replace("/", "_")
            self.parameters_order.append("name")
        if (type is not None) & (type != ""):
            self.type = type
            self.parameters_order.append("type")

    def set_position_for_unnamed(self, table_name, field_name):
        self.position_for_unnamed = []
        self.position_for_unnamed.append(table_name)
        self.position_for_unnamed.append(field_name)

    def set_name(self, name):
        if (name is not None) & (name != ""):
            self.name = name.replace(" ", "_").\
                replace("\\", "_")\
                .replace("-", "_").\
                replace(".", "").\
                replace("/", "_")
            self.parameters_order.append("name")

    def get_name(self):
        return self.name

    def set_type(self, type):
        if (type is not None) & (type != ""):
            self.type = type
            self.parameters_order.append("type")

    def get_type(self):
        return self.type

    def set_align(self, align):
        if (align is not None) & (align != ""):
            self.align = list(align).pop(0)
            self.parameters_order.append("align")

    def get_align(self):
        return self.align

    def set_width(self, width):
        if (width is not None) & (width != ""):
            self.width = int(width)
            self.parameters_order.append("width")

    def get_width(self):
        return self.width

    def set_char_length(self, char_length):
        if (char_length is not None) & (char_length != ""):
            self.char_length = int(char_length)
            self.parameters_order.append("char_length")

    def get_char_length(self):
        return self.char_length

    def set_description(self, description):
        if (description is not None) & (description != ""):
            self.description = description
            self.parameters_order.append("description")

    def get_description(self):
        return self.description

    def set_props(self, props):
        props_temp = []
        for prop in props.split(","):
            props_temp.append(prop.strip())
        if (props_temp is not None) & (len(props_temp) != 0):
            self.parameters_order.append("props")
        props_temp_set = set(props_temp)
        props_temp.clear()
        for p in props_temp_set:
            if not(p == ""):
                props_temp.append(p)
        self.props = set(props_temp)


    def get_props(self):
        return self.props

    def if_prop_exists(self, prop):
        if (prop in self.props):
            return True
        else:
            return False

    def set_precision(self, precision):
        if (precision is not None) & (precision != ""):
            self.precision = int(precision)
            self.parameters_order.append("precision")

    def get_precision(self):
        return self.precision

    def set_scale(self, scale):
        if (scale is not None) & (scale != ""):
            self.scale = int(scale)
            self.parameters_order.append("scale")

    def get_scale(self):
        return self.scale

    def set_length(self, length):
        if (length is not None) & (length != ""):
            self.length = int(length)
            self.parameters_order.append("length")

    def get_length(self):
        return self.length
