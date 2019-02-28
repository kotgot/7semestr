from utils.XmlParser import *
from utils.DBInitializer import *
from utils.RAMToDBDConverter import *
import os

DATABASE_NAME = "database.db"
XML_FILE_NAME_1 = "./resources/tasks.xml"
XML_FILE_NAME_2 = "./resources/prjadm.xml"

schemas = create_list_of_objects_from_xml([XML_FILE_NAME_1, XML_FILE_NAME_2])

create = not os.path.exists(DATABASE_NAME)
if create:
    initializer = DBInitializer(DATABASE_NAME)
    initializer.init_database()
    converter_to_database = RAMToDBDConverter(DATABASE_NAME)
    converter_to_database.RAM_to_DBD(schemas)





