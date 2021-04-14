import sql_database as sql

# count how many student there are

student_count = """SELECT COUNT(name) FROM student"""

print('Student count: \n', sql.sql_query(student_count).fetchall())


# create a table with all the students that made an NLP project

nlp_table = """SELECT student.name FROM student, project WHERE student.id = project.St AND project.Topic = 'nlp'"""

print('Student that made a NLP project: \n', sql.pandas_select(nlp_table))


# create a table with all the teachers specialized in ML that makes more than 1200

rich_ml = """SELECT name FROM teacher WHERE speciality = 'Machine Learning' AND salary > 1200"""

print('ML Teacher that makes more than 1200€: \n', sql.pandas_select(rich_ml))


# add a new field in student that references their favorite teacher

fav_teacher = """ALTER TABLE student
                ADD COLUMN fav_teacher varchar(20)"""

sql.sql_execute(fav_teacher)
print(sql.pandas_select("""SELECT * FROM STUDENT"""))

# delete all the students that have a name starting with 'j' and ending with 'n'

del_char = """SELECT name FROM student where name NOT LIKE 'J%n'"""
print('Removing Jon from the list of names \n', sql.pandas_select(del_char))


# count how many unique students names there are

unique_count = """SELECT DISCTINCT(name) FROM student"""
print('Count of the unique names: \n', sql.sql_query(student_count).fetchall())


# join the tables project and student

joined = """SELECT * FROM student INNER JOIN project ON student.id = project.St"""
print('Project and student joined:', sql.pandas_select(joined))

# get the name of the students with the higher grade on a project

high = """SELECT student.name FROM student, project WHERE student.id = project.St AND max(project.Grade)"""
print('Highest graded student: \n', sql.pandas_select(high))
