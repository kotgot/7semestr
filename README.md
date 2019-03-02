# 7semestr
Учебный проект по дисциплине "Коллективная разработка приложений"
# Структура проекта
+ db_sources
	+ `DBClasses.py` - содержит в себе описание классов для представления объектов базы данных в RAM.
		 - Schema; - класс схемы БД
		 - Table; - класс table 
		 - Field; - класс field 
		 - Domain; - класс domain 
		 - Constraint; -- класс Constraint
		 - Index. - класс index 
	+ `DBDConst.py` - содержит в себе DDL базы данных.
+ sources_xmls
    + `PRJADM.xml` - файл с xml описателем `PRJADM` схемы БД
    + `TASKS.xml` - файл с xml описателем `TASKS` схемы БД
+ utils
    + `RAM_to_DBD.py` - содержит функции для вставки в таблицы БД
	+ `DBD_to_RAM.py` - содержит класс для переноса DBD в RAM
	+ `RAM_to_XDB.py` - содержит функции для вставки в таблицы БД
	+ `XDB_to_RAM.py` - содержит класс для переноса XDB в RAM
	+ `minidom_fixed.py` - попытка исправления недостатка xml.dom.minidom, состоящего в том, что xml.dom.mindom.Document.writexml не сохраняет последовательность атрибутов тэга;
	+ `helpers.py` - набор функций для отладки;
	+ `RAM_to_PostgreSQL.py` - содержит класс, который переводит представление RAM в PostgreSQL DDL.
	+ `MSSQL_to_RAM.py` - класс,который содержит функции для получения метаданных из MS SQL в RAM
	+ `MSSQLToPostgreSQLDataTranslator.py` - передача данных транзакции из ms sql в postgresql
+ `main.py` - главное приложение
+ `mssql2pg.py`
+ `mssql2xml.py`
+ `dbd2xdb.py`
+ `xdb2dbd.py`
