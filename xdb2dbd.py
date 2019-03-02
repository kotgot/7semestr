import os
import xml.dom.minidom as md
from data_base_sources.DBD_const import SQL_DBD_Init
from utils.XML_to_RAM import XMLToRAMConverter
from utils.RAM_to_DBD import RAMToDBDConverter


xml = md.parse(os.path.join("./source_xmls", "TASKS.xml"))

dbd_repr = RAMToDBDConverter(XMLToRAMConverter(xml).xml_to_ram(), "tasks.db", SQL_DBD_Init).ram_to_dbd()
