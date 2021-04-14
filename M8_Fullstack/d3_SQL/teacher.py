import sql_database

teacher = """CREATE TABLE IF NOT EXISTS teacher (
                name VARCHAR(20),
                surname VARCHAR(20) NOT NULL,
                id int NOT NULL PRIMARY KEY,
                country VARCHAR(20),
                speciality VARCHAR(20) NOT NULL,
                salary int,
                FOREIGN KEY(id) REFERENCES project(st)
        );"""


sql_database.sql_execute(teacher)

teachers = """INSERT INTO teacher(name, surname, id, country, speciality, salary)
                VALUES ('Jan', 'Carbonell', 01, 'Spain', 'The Boss', 100000000),
                        ('Antonio', 'Marsella', 02, 'Italy', 'Math', 800),
                        ('Javier', 'Perez', 03, 'Portugal', 'Machine Learning', 1150),
                        ('George', 'Studentko', 04, 'Poland', 'Computer Vision', 900),
                        ('Jon', 'Perez', 05, 'Spain', 'SQL', 1200),
                        ('Mark', 'Antonio', 06, 'U.K.', 'Python', 1400),
                        ('Pasquale', 'Cicciomicio', 07, 'Italy', 'NLP', 750),
                        ('Louis', 'Blater', 08, 'France', 'Deep Learning', 2120),
                        ('Pier', 'Marillo', 09, 'Switzerland', 'PE', 1100),
                        ('Herman', 'Mann', 10, 'German', 'Administration', 1320)"""

sql_database.sql_execute(teachers)

df = sql_database.pd_select("select * from teacher")
print(df)
sql_database.close()
