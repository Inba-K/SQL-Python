import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Inbezerman!10",
    database="stud_db"
)

cursor=db.cursor()
sql=("Select MAX(age) From students")
cursor.execute(sql)
result=cursor.fetchone()
print(result)

cursor.close()
db.close()