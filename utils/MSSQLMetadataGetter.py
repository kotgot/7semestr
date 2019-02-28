import pyodbc
from classes.DBDSchema import DBDSchema
from classes.Table import Table
from classes.Field import Field
from classes.Domain import Domain
from classes.Constraint import Constraint
from classes.Index import Index


class MSSQLMetadataGetter:
    connection = None
    cursor = None

    def __init__(self):
        print("start")
        try:
            self.connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                                             "Server=noutdexp\sqlexpress;" +
                                             "Database=northwind;" +
                                             "uid=mssqluser;" +
                                             "pwd=123;")
            self.cursor = self.connection.cursor()
        except (Exception) as error:
            print("Error while connecting to MS SQL", error)

    def get_metadata(self, schema_name):
        try:
            if (self.schema_exists(schema_name)):
                schema = DBDSchema(None)  # no fulltext_engine
                schema.set_name(schema_name)
                tables = []
                for t in self.cursor.tables(schema=schema_name, tableType='TABLE'):
                    if (t.table_name != "sysdiagrams"):  # exclude system table
                        table = Table(t.table_name.replace(" ", "_"))
                        table.set_description(t.remarks)
                        tables.append(table)

                for table in tables:
                    for column in self.cursor.columns(schema=schema_name):
                        if (column.table_name.replace(" ", "_") == table.name):
                            field = Field(column.column_name, column.ordinal_position)
                            field.set_description(column.remarks)

                            domain_name = "Unnamed_" + table.name + "_" + field.name
                            domain = Domain(domain_name, column.type_name, True)
                            if ((domain.type == "nvarchar") or (domain.type == "ntext")):
                                domain.set_char_length(column.column_size)
                            domain.set_width(column.column_size)
                            domain.set_position_for_unnamed(table.name, field.name)
                            field.set_domain(domain.name)
                            schema.set_domain(domain.name, domain)

                            table.set_field(field.name, field)

                    firstly_met = True
                    i = 1
                    for pk in self.cursor.primaryKeys(schema=schema_name, table=table.name.replace("_", " ")):
                        primary_key = Constraint("PRIMARY", i)
                        if (firstly_met):
                            primary_key.set_name(pk.pk_name)
                            firstly_met = False
                        else:  # Add postfix to composite pk name
                            primary_key.set_name(pk.pk_name + "_Reiteration_" + str(i))
                            i += 1
                        primary_key.set_items(pk.column_name)
                        table.set_constraint(primary_key)

                    names = []
                    inds = {}
                    for ind in self.cursor.statistics(schema=schema_name, table=table.name.replace("_", " ")):
                        if (ind.index_name is not None):
                            if (names.count(ind.index_name) == 0):
                                index = Index(ind.column_name, ind.ordinal_position)
                                index.set_name(ind.index_name)
                                names.append(index.name)
                                if (ind.non_unique == 0):
                                    index.set_props("uniqueness")
                                inds[ind.index_name] = index
                                names.append(index.name)
                            else:
                                temp = inds[ind.index_name]
                                temp.set_field_name(temp.field_name + ", " + ind.column_name)
                                inds[ind.index_name] = temp

                    for index in inds.values():
                        table.set_index(index)

                    schema.set_table(table)

                for table in tables:
                    i = 0
                    for pk in schema.get_table(table.name).get_constraints():
                        if (pk.kind == "PRIMARY"):
                            i += 1
                    for fk in self.cursor.foreignKeys(schema=schema_name, table=table.name):
                        foreign_key = Constraint("FOREIGN", i)
                        foreign_key.set_reference(table.name)
                        foreign_key.set_name(fk.fk_name)
                        foreign_key.set_items(fk.fkcolumn_name)
                        if (fk.delete_rule == 1):
                            foreign_key.set_props("cascading_delete")
                        temp_table = schema.get_table(fk.fktable_name.replace(" ", "_"))
                        temp_table.set_constraint(foreign_key)
                        schema.set_table(temp_table)
                        i += 1
                return schema
            else:
                return None
        except (Exception) as error:
            print("Error while connecting to MS SQL", error)
        finally:
            if (self.connection):
                self.cursor.close()
                self.connection.close()
                print("MS SQL connection is closed")

    def schema_exists(self, schema_name):
        self.cursor.execute("""select name from sys.schemas where name=?""", (schema_name))
        row = self.cursor.fetchone()
        if (row.name == schema_name):
            print("Схема найдена")
            return True
        else:
            return False