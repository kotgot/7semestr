from xml.dom import minidom
from classes.DBDSchema import DBDSchema
from classes.Domain import Domain
from classes.Table import Table
from classes.Field import Field
from classes.Constraint import Constraint
from classes.Index import Index


def create_list_of_objects_from_xml(paths):
    schemas = []
    for path in paths:
        doc = minidom.parse(path)
        xml_schema = doc.getElementsByTagName("dbd_schema")[0]
        schema = DBDSchema(xml_schema.getAttribute("fulltext_engine"))
        schema.set_version(xml_schema.getAttribute("version"))
        schema.set_name(xml_schema.getAttribute("name"))
        schema.set_description(xml_schema.getAttribute("description"))

        xml_domains = doc.getElementsByTagName("domain")
        for xml_domain in xml_domains:
            domain_name = xml_domain.getAttribute("name")
            if (schema.get_domain(domain_name) is None):
                domain = Domain(domain_name,
                                xml_domain.getAttribute("type"), False)
                domain.set_align(xml_domain.getAttribute("align"))
                domain.set_width(xml_domain.getAttribute("width"))
                domain.set_char_length(xml_domain.getAttribute("char_length"))
                domain.set_description(xml_domain.getAttribute("description"))
                domain.set_props(xml_domain.getAttribute("props"))
                domain.set_precision(xml_domain.getAttribute("precision"))
                domain.set_length(xml_domain.getAttribute("length"))
                domain.set_scale(xml_domain.getAttribute("scale"))
                schema.set_domain(domain.name, domain)

        xml_tables = doc.getElementsByTagName("table")
        for xml_table in xml_tables:
            table = Table(xml_table.getAttribute("name"))
            table.set_description(xml_table.getAttribute("description"))
            table.set_props(xml_table.getAttribute("props"))
            table.set_ht_table_flags(xml_table.getAttribute("ht_table_flags"))
            table.set_access_level(xml_table.getAttribute("access_level"))

            xml_fields = xml_table.getElementsByTagName("field")
            position = 1
            for xml_field in xml_fields:
                field = Field(xml_field.getAttribute("name"), position)
                field.set_rname(xml_field.getAttribute("rname"))

                if ((xml_field.getAttribute("type") is not None) and
                        (xml_field.getAttribute("type") != "")):
                    domain = Domain("Unnamed_" + xml_table.getAttribute("name") +
                                    "_" + xml_field.getAttribute("name"),
                                    xml_field.getAttribute("type"), True)
                    domain.set_position_for_unnamed(xml_table.getAttribute("name"),
                                                    xml_field.getAttribute("name"))
                    domain.set_align(xml_field.getAttribute("align"))
                    domain.set_width(xml_field.getAttribute("width"))
                    domain.set_char_length(xml_field.getAttribute("char_length"))
                    domain.set_description(xml_field.getAttribute("description"))
                    domain.set_props(xml_field.getAttribute("type_props"))
                    domain.set_precision(xml_field.getAttribute("precision"))
                    domain.set_length(xml_field.getAttribute("length"))
                    domain.set_scale(xml_field.getAttribute("scale"))
                    schema.set_domain(domain.name, domain)
                    field.set_domain(domain.name)
                else:
                    field.set_domain(xml_field.getAttribute("domain"))

                field.set_description(xml_field.getAttribute("description"))
                field.set_props(xml_field.getAttribute("props"))
                table.set_field(field.name, field)
                position += 1

            position = 1
            xml_constraints = xml_table.getElementsByTagName("constraint")
            for xml_constraint in xml_constraints:
                constraint = Constraint(xml_constraint.getAttribute("kind"), position)
                constraint.set_props(xml_constraint.getAttribute("props"))
                constraint.set_reference(xml_constraint.getAttribute("reference"))
                constraint.set_items(xml_constraint.getAttribute("items"))
                table.set_constraint(constraint)
                position += 1

            position = 1
            xml_indices = xml_table.getElementsByTagName("index")
            for xml_index in xml_indices:
                index = Index(xml_index.getAttribute("field"), position)
                index.set_props(xml_index.getAttribute("props"))
                table.set_index(index)
                position += 1

            schema.set_table(table)
        schemas.append(schema)
    return schemas
