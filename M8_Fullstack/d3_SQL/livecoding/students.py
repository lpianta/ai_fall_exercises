import sql_interface as sql
import sqlite3
import pandas as pd

create_student_table = """CREATE TABLE student(
                           name char(20) NOT NULL,
                           surname char(20) NOT NULL,
                           id int NOT NULL PRIMARY KEY,
                           country char(20),
                           FOREIGN KEY(id) REFERENCES projects (st)
                           );
                         """

create_student = """INSERT INTO
                  student(name, surname, id)
                  VALUES('tobias', 'schulz', 00);
                  """

select = "SELECT * FROM students"

drop_table = "DROP TABLE student"


sql.sql_query(create_student_table)
sql.sql_query(create_student)

print(sql.sql_query("SELECT * FROM student").fetchall())

