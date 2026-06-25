import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Inbezerman!10',
    database='library'
)

cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Students(student_id primary key,Name varchar(255),Grade int)""")

student_id=int(input("Enter the student id: "))
Name=input("Enter the student's name: ")
Grade=int(input("Enter the grade of the student: "))

sql=("Insert Into Students(student_id,Name,Grade)Values(%s,%s,%s)")
values=(student_id,Name,Grade)
cursor.execute(sql,values)

db.commit()
print("Student details added!")

cursor.close()
db.close()