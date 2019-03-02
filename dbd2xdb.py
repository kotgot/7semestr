from utils.DBD_to_RAM import DBDToRAMConverter
from utils.RAM_to_XDB import RAMToXMLConverter

xml_repr = RAMToXMLConverter(DBDToRAMConverter("tasks.db").fetch_schema()).ram_to_xml()
with open("./tasks.xml", "wb") as f:
    f.write(xml_repr.toprettyxml(encoding="utf-8", indent="  "))
