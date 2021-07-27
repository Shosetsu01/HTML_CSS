Создание соединения
import sqlite3

con = sqlite3.connect('mydatabase.db')

Создание базы данных
import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect(':memory:')

        print("Connection is established: Database is created in memory")

    except Error:

        print(Error)

    finally:

        con.close()

sql_connection()

Создание таблицы
employees (id, name, salary, department, position, hireDate)

import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, 

name text, salary real, department text, position text, hireDate 

text)")

    con.commit()

con = sql_connection()

sql_table(con)

Вставка данных в таблицу
cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")

cursorObj.execute('''INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)''', entities)

entity = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_insert(con, entities):

    cursorObj = con.cursor()

    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)

    con.commit()

entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

sql_insert(con, entities)
Обновление таблицы
import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_update(con):

    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')

    con.commit()

sql_update(con)
Оператор SELECT
select * from table_name

cursorObj.execute('SELECT * FROM employees ')

select column1, column2 from tables_name

cursorObj.execute('SELECT id, name FROM employees')
Выборка всех данных:
import sqlite3
con = sqlite3.connect('mydatabase.db')
def sql_fetch(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)

 [print(row) for row in cursorObj.fetchall()]

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
Удаление таблицы
drop table table_name

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()

sql_fetch(con)



import sys

from PyQt4 import QtGui
def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle(“PyQt”)
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
