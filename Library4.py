def Menu_4():
    import mysql.connector
    from datetime import datetime,timedelta
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Inbezerman!10',
        database='library'
    )

    cursor=db.cursor()
    book_id=input("Enter the book id: ")

    sql=("Select * From Books Where book_id=%s and available_copies!=0")
    values=(book_id,)
    cursor.execute(sql,values)

    result=cursor.fetchall()
    if len(result)==0:
        print("This book isn't available...")
    else:
        availability=result[0][4]
        availability=availability-1

        Name=input("Enter the student's name: ")
        Title=input("Book which is being borrowed: ")
        issue_date=datetime.now().date()
        return_date=issue_date+timedelta(days=15)

        sql=("Insert Into Transactions(Name,Title,issue_date,return_date)Values(%s,%s,%s,%s)")
        values=(Name,Title,issue_date,return_date)
        cursor.execute(sql,values)

        sql1=("Update Books Set available_copies=available_copies-1 Where book_id=%s")
        values1=(book_id,)
        cursor.execute(sql1,values1)
        print("Book Issued!")
        db.commit()

    cursor.close()
    db.close()