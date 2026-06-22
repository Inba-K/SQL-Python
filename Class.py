import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Inbezerman!10',
    database='class_monitor'
)

cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS class (id int primary key, name varchar(255) not null,age int default 14)""")
id=int(input("Enter a number: "))
name=input("Enter a name: ")
age=int(input("Enter a number: "))
sql=("Insert Into class(id,name,age)Values(%s,%s,%s)")
values=(id,name,age)
cursor.execute(sql,values)
db.commit()
print("Data Inserted Successfully!")
cursor.close()
db.close()