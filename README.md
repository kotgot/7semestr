# educational-project
Учебный проект по дисциплине "Коллективная разработка приложений"
# Структура проекта
+ classes
    + `Constraint.py` - класс Constraint
    + `DBDSchema.py` - класс схемы БД
    + `Domain.py` - класс domain 
    + `Field.py` - класс field 
    + `Index.py` - класс index 
    + `Table.py` - класс table 
+ resources
    + `prjadm.xml` - файл с xml описателем `PRJADM` схемы БД
    + `tasks.xml` - файл с xml описателем `TASKS` схемы БД
+ utils
    + `XmlParser.py` - содержит функцию `create_list_of_objects_from_xml` которая создает классы из xml описания
    + `DBInitializer.py` - класс,который содержит функцию для инициализации базы данных
    + `RAMToDBDConverter.py` - содержит функции для вставки в таблицы БД
    + `DDLPostgreSQLGenerator.py` - класс, который содержит функции для генерации PostgreSQL ddl
    + `MSSQLMetadataGetter.py` - класс,который содержит функции для получения метаданных из MS SQL в RAM
    + `MSSQLToPostgreSQL.py` - передача данных транзакции из ms sql в postgresql
    + `RAMToXDBConverter.py` - содержит функции для вставки в таблицы БД
+ `MainApplication.py` - главное приложение
