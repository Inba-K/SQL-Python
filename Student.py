import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Inbezerman!10",
    database="stud_db"
)

cursor=db.cursor()
roll_number=int(input("Enter a number:"))
name=input("Enter the name:")

sql=("Update students SET name=%s where roll_number=%s")
values=(name,roll_number)

cursor.execute(sql,values)

db.commit()
cursor.close()
db.close()