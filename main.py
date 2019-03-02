import os
import xml.dom.minidom as md
from utils.XML_to_RAM import XMLToRAMConverter
from utils.RAM_to_XML import RAMToXMLConverter
from utils.RAM_to_DBD import RAMToDBDConverter
from utils.DBD_to_RAM import DBDToRAMConverter
from db_sources.DBD_const import SQL_DBD_Init


xml = md.parse(os.path.join("source_xmls/", "TASKS.xml"))
schema = XMLToRAMConverter(xml).xml_to_ram()

xml1 = RAMToXMLConverter(schema).ram_to_xml()
with open("./tasks.xml", "wb") as f:
    f.write(xml1.toprettyxml(encoding="utf-8", indent="  "))

conv = RAMToDBDConverter(schema, "tasks.db", SQL_DBD_Init).ram_to_dbd()
schema = DBDToRAMConverter("tasks.db").dbd_to_ram()