import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Inbezerman!10",
    database="stud_db"
)

cursor=db.cursor()
sql=("Select COUNT(roll_number),age From students Group By age")
cursor.execute(sql)
result=cursor.fetchall()
print(result)

cursor.close()
db.close()