import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Inbezerman!10",
    database="stud_db"
)

cursor=db.cursor()
name=input("Enter the name:")

sql=("Delete From Students where name=%s")
values=(name,)

cursor.execute(sql,values)

db.commit()
cursor.close()
db.close()