from datetime import datetime

import pyodbc
import psycopg2
from pip._vendor.pyparsing import basestring
from psycopg2 import sql
from classes.DBDSchema import DBDSchema
from classes.Table import Table
from classes.Field import Field
from classes.Domain import Domain
from classes.Constraint import Constraint
from classes.Index import Index
from utils.MSSQLMetadataGetter import *
from utils.DDLPostgreSQLGenerator import *

USERNAME = "postgres"

def main(schema):
    try:
        ms_sql_to_postgresql(schema)
    except (Exception) as error:
        print("Error: ", error)

def ms_sql_to_postgresql(schema):
    connection_ms = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                                     "Server=noutdexp\sqlexpress;" +
                                     "Database=northwind;" +
                                     "uid=mssqluser;" +
                                     "pwd=123;")
    cursor_ms = connection_ms.cursor()
    connection_postgres = psycopg2.connect(host="localhost",
                                       port="5432",
                                       database="mydb",
                                       user=USERNAME,
                                       password="postgres")
    cursor_postgres = connection_postgres.cursor()
    schema_name = schema.name
    cursor_postgres.execute("START TRANSACTION DEFERRABLE")

    for table in schema.get_tables().values():
        query_ms = "SELECT "
        firstly_met = True
        quantity = 0
        fields_query = ""
        for field in table.get_fields().values():
            if (firstly_met):
                query_ms += field.name
                fields_query += field.name
                firstly_met = False
                quantity += 1
            else:
                quantity += 1
                query_ms += ", " + field.name
                fields_query += ", " + field.name
        query_ms += " FROM " + schema_name + "." + table.name.replace("_", " ")

        cursor_ms.execute(query_ms)
        rows = cursor_ms.fetchall()
        cursor_postgres.execute("""SET CONSTRAINTS ALL DEFERRED""")

        for row in rows:
            query_postgres = "INSERT INTO " + schema_name + "." + table.name + " ("
            query_postgres += fields_query + ") VALUES ("
            firstly_met = True
            for q in range(quantity):
                if (firstly_met):
                    if (row[q] is not None):
                        if ((isinstance(row[q], basestring))):
                            query_postgres += "'" + row[q].replace("'", "") + "'"
                        elif (isinstance(row[q], datetime)):
                            query_postgres += "'" + str(row[q]) + "'"
                        elif ((isinstance(row[q], bytearray)) or (isinstance(row[q], bytes))):
                            part = str(row[q])[2:-1].replace("'", "").replace("\"", "")
                            query_postgres += "'" + part + "'"
                        else:
                            query_postgres += str(row[q])
                    else:
                        query_postgres += "NULL"
                    firstly_met = False
                else:
                    if (row[q] is not None):
                        if ((isinstance(row[q], basestring))):
                            query_postgres += ", '" + row[q].replace("'", "") + "'"
                        elif (isinstance(row[q], datetime)):
                            query_postgres += ", '" + str(row[q]) + "'"
                        elif ((isinstance(row[q], bytearray)) or (isinstance(row[q], bytes))):
                            part = str(row[q])[2:-1].replace("'", "").replace("\"", "")
                            query_postgres += ", '" + part + "'"
                        else:
                            query_postgres += ", " + str(row[q])
                    else:
                        query_postgres += ", NULL"
            query_postgres += ")"
            print(query_postgres)
            cursor_postgres.execute("""SET CONSTRAINTS ALL DEFERRED""")
            cursor_postgres.execute(sql.SQL(query_postgres))
            connection_postgres.commit()

            print("----------------")
    cursor_ms.close()
    connection_ms.close()
    cursor_postgres.close()
    connection_postgres.close()



