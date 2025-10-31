import sqlite3

# connect to sqlite
connection=sqlite3.connect("student.db")

# create a cursorobject to insert record.create table
cursor=connection.cursor()

# create the table
table_info="""
create table STUDENT (NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## insert some more records
cursor.execute('''Insert Into STUDENT values('krish','Data science','A','90')''')
cursor.execute('''Insert Into STUDENT values('john','Data science','B','100')''')
cursor.execute('''Insert Into STUDENT values('mukesh','Data science','A','86')''')
cursor.execute('''Insert Into STUDENT values('jacob','devops','A','50')''')
cursor.execute('''Insert Into STUDENT values('dipesh','devops','A','35')''')

# display all the record
print("The insert records are ")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# commit your changes in the database 
connection.commit()
connection.close()

