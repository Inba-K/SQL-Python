import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Inbezerman!10',
    database='library'
)

cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Transactions(Name varchar(255),Title varchar(255),issue_date varchar(255),return_date varchar(255))""")

db.commit()
cursor.close()
db.close()