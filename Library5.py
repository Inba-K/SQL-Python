def Menu_5():
    import mysql.connector
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Inbezerman!10',
    database='library'
    )

    cursor=db.cursor()
    sql=("Select * From Books")
    cursor.execute(sql,)
    result=cursor.fetchall()
    print("These are the books we have:")
    print(result)
    
    cursor.close()
    db.close()