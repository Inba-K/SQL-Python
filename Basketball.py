import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Inbezerman!10',
    database='basketball'
)

cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS basketball (id int primary key,name varchar(255),best_player varchar(255) unique,points int)""")

id=int(input("Enter the team id: "))
name=input("Enter the name of the team: ")
best_player=input("Who is this team's best player? ")
points=int(input("How many points have they scored? "))

sql=("Insert Into basketball(id,name,best_player,points)Values(%s,%s,%s,%s)")
values=(id,name,best_player,points)
cursor.execute(sql,values)
db.commit()
print("Data inserted successfully!")
cursor.close()
db.close()