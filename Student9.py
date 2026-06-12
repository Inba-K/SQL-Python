import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Inbezerman!10",
    database="stud_db"
)

cursor=db.cursor()
sql=("Select * From students Order By name")
cursor.execute(sql)
result=cursor.fetchall()
print(result)

cursor.close()
db.close()