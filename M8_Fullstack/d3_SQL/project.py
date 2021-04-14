import sql_database

project = """CREATE TABLE IF NOT EXISTS project (
                NameP VARCHAR(20),
                Topic VARCHAR(20) NOT NULL,
                St int NOT NULL,
                id int NOT NULL PRIMARY KEY,
                tch VARCHAR(20) NOT NULL,
                FOREIGN KEY(st) REFERENCES student(id) ON UPDATE RESTRICT
                FOREIGN KEY(tch) REFERENCES teachers(id) ON UPDATE RESTRICT
        );"""


sql_database.sql_execute(project)

sql_database.pd_upload_csv('project', './Dataset/project.csv')

df = sql_database.pd_select("select * from project")
print(df)
sql_database.close()
