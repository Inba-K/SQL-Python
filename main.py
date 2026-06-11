import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Inbezerman!10",
    database="stud_db"
)


cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students (roll_number int,name varchar(255),age int) """)
roll=int(input("Enter the roll_number  "))
name=input("Enter the name ")
age=int(input("Enter the age: "))


sql="Insert into students (roll_number,name,age) Values(%s,%s,%s)"
values=(roll,name,age)
cursor.execute(sql,values)
db.commit()
print("Data inserted succesfully")




cursor.execute("SELECT * FROM students")
result=cursor.fetchall()
print(result)






cursor.close()
db.close()
