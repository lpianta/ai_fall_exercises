import sql_database

student = """CREATE TABLE IF NOT EXISTS student (
                name VARCHAR(20) PRIMARY KEY,
                surname VARCHAR(20) NOT NULL,
                id int NOT NULL,
                country VARCHAR(20),
                FOREIGN KEY(id) REFERENCES project(st) ON UPDATE CASCADE
        );"""


sql_database.sql_execute(student)

jon = """INSERT INTO student (name, surname, id, country) VALUES ('Jon', 'Smith', 01, 'U.K.')"""
luca = """INSERT INTO student (name, surname, id, country) VALUES ('Luca', 'Pianta', 02, 'Italy')"""
sai = """INSERT INTO student (name, surname, id, country) VALUES ('Sai', 'Dailli', 03, 'India')"""
kim = """INSERT INTO student (name, surname, id, country) VALUES ('Kim', 'Jones', 04, 'Norway')"""
lorenzo = """INSERT INTO student (name, surname, id, country) VALUES ('Lorenzo', 'Miride', 05, 'Italy')"""
martin = """INSERT INTO student (name, surname, id, country) VALUES ('Martin', 'Tavarez', 06, 'Spain')"""
bence = """INSERT INTO student (name, surname, id, country) VALUES ('Bence', 'Kovack', 07, 'Portugal')"""
tobias = """INSERT INTO student (name, surname, id, country) VALUES ('Tobias', 'Schulz', 08, 'Germany')"""
joby = """INSERT INTO student (name, surname, id, country) VALUES ('Joby', 'Inngram', 09, 'U.K.')"""
aderemi = """INSERT INTO student (name, surname, id, country) VALUES ('Aderemi', 'Smith', 10, 'Portugal')"""

sql_database.sql_execute(jon)
sql_database.sql_execute(luca)
sql_database.sql_execute(sai)
sql_database.sql_execute(kim)
sql_database.sql_execute(lorenzo)
sql_database.sql_execute(martin)
sql_database.sql_execute(bence)
sql_database.sql_execute(tobias)
sql_database.sql_execute(joby)
sql_database.sql_execute(aderemi)


df = sql_database.pd_select("select * from student")
print(df)
sql_database.close()
