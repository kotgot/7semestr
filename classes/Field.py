class Field:
    parameters_order = None  # list of names of field parameters, will be useful when RAM->XML
    name = None
    rname = None
    domain = None  # name of Domain
    props = None
    position = None
    description = None

    def __init__(self, name, position):
        self.parameters_order = []
        if (name is not None) & (name != ""):
            self.name = name
            self.parameters_order.append("name")
        if (position is not None) & (position != ""):
            self.position = int(position)

    def set_name(self, name):
        if (name is not None) & (name != ""):
            self.name = name
            self.parameters_order.append("name")

    def get_name(self):
        return self.name

    def set_rname(self, rname):
        if (rname is not None) & (rname != ""):
            self.rname = rname
            self.parameters_order.append("rname")

    def get_rname(self):
        return self.rname

    def set_domain(self, domain):
        if (domain is not None) & (domain != ""):
            self.domain = domain.replace(" ", "_").\
                replace("\\", "_")\
                .replace("-", "_").\
                replace(".", "").\
                replace("/", "_")
            self.parameters_order.append("domain")

    def get_domain(self):
        return self.domain

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

    def set_description(self, description):
        if (description is not None) & (description != ""):
            self.description = description
            self.parameters_order.append("description")

    def get_description(self):
        return self.description