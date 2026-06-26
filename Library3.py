def Menu_3():
    import mysql.connector
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Inbezerman!10',
        database='library'
    )

    cursor=db.cursor()
    id=int(input("Enter the id of the book you will restock: "))
    Name=input("Enter the name of the student: ")

    sql=("Update Books Set available_copies=available_copies+1 Where book_id=%s")
    values=(id,)
    cursor.execute(sql,values)
    sql1=("Delete From Transactions Where Name=%s")
    values1=(Name,)
    cursor.execute(sql1,values1)

    db.commit()
    print("Book restocked!")

    cursor.close()
    db.close()