class Constraint:
    parameters_order = None  # list of names of constraints parameters, will be useful when RAM->XML
    kind = None
    items = None  # field name
    reference = None  # table name
    props = None
    position = None
    name = None

    def __init__(self, kind, position):
        self.parameters_order = []
        if (kind is not None) & (kind != ""):
            self.kind = kind
            self.parameters_order.append("kind")
        if (position is not None) | (position != ""):
            self.position = int(position)

    def set_kind(self, kind):
        if (kind is not None) & (kind != ""):
            self.kind = kind
            self.parameters_order.append("kind")

    def getKind(self):
        return self.kind

    def set_name(self, name):
        if (name is not None) & (name != ""):
            self.name = name
            self.parameters_order.append("name")

    def get_name(self):
        return self.name

    def set_reference(self, reference):
        if (reference is not None) & (reference != ""):
            self.reference = reference
            self.parameters_order.append("reference")

    def get_reference(self):
        return self.reference

    def set_props(self, props):
        props_temp = []
        for prop in props.split(","):
            props_temp.append(prop.strip())
        if (props_temp is not None) & (len(props_temp) != 0):
            self.parameters_order.append("props")
        props_temp_set = set(props_temp)
        props_temp.clear()
        for p in props_temp_set:
            if not (p == ""):
                props_temp.append(p)
        self.props = set(props_temp)

    def get_props(self):
        return self.props

    def if_prop_exists(self, prop):
        if (prop in self.props):
            return True
        else:
            return False

    def set_items(self, items):
        if (items is not None) & (items != ""):
            self.items = items
            self.parameters_order.append("items")

    def get_items(self):
        return self.items
