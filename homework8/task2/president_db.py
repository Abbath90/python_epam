"""Homework 2:
Preamble
We have a database file (example.sqlite) in sqlite3 format with some tables and data.
All tables have 'name' column and maybe some additional ones.

Data retrieval and modifications are done with sqlite3 module by issuing SQL statements.
For example, to get all data from TABLE1:

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * from TABLE1')
data = cursor.fetchall()   # will be a list with data.
instead of getting all data at once, you can use .fetchone() calls and named expressions:

while row:=cursor.fetchone():
    print(row)
To get a row with specific name equal to some value:

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * from presidents where name=:name', {name:'Yeltsin'})
data = cursor.fetchall()  # will get all records with this name.
You can also use .fetchone() to get one record.
in order to get record with first name (sorted alphabetically) use SQL expression
SELECT * from presidents order by name asc limit 1
in order to get record after specified (sorted alphabetically) use SQL expression
SELECT * from presidents where name > :name order by name limit.
To get amount of records in table TABLE1, use select count(*) from TABLE1 query.

Please refer to this documents for more information about how to retrieve
data from sqlite database: DBAPI: https://www.python.org/dev/peps/pep-0249/
sqlite3 module: https://docs.python.org/3/library/sqlite3.html

Task
Write a wrapper class TableData for database table, that when initialized
with database name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
len(presidents) will give current amount of rows in presidents table in database
presidents['Yeltsin'] should return single data row for president with name Yeltsin
'Yeltsin' in presidents should return if president with same name exists in table
object implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data. If data in
table changed after you created collection instance, your calls should
return updated data.
Avoid reading entire table into memory. When iterating through records,
start reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file."""

import sqlite3

class TableData:
    def __init__(self, database_name, table_name):
        self.open_db(database_name)
        db_data = self.get_table(table_name)
        tabledata_dict = self.form_tabledata_dict(db_data)
        for name in tabledata_dict:
            setattr(self, name, tabledata_dict[name])


    def open_db(self, name):
        try:
            self.conn = sqlite3.connect(name);
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print("Error connecting to database!")

    def get_table(self, table, columns = '*', limit=None):
        query = f"SELECT {columns} from {table};"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return rows[len(rows)-limit if limit else 0:]

    def form_tabledata_dict(self, db_data):
        return {dataset[0]: [dataset[1], dataset[2]] for dataset in db_data}



    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __contains__(self, key):
        return key in self.__dict__

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        if isinstance(key, (int, float)) or key.isdigit():
            raise ValueError("Invalid key")
        else:
            self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]


if __name__ == "__main__":
    q = TableData('example.sqlite', 'presidents')
    print(q.__dict__)
    print(q['Yeltsin'])
    print('Yeltsin' in q)
    for president in q:
        print(president)
    #Табличная структура???
