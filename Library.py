def Menu_1():
    import mysql.connector
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Inbezerman!10',
        database='library'
    )

    cursor=db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Books(book_id int primary key,Title varchar(255) not null,Author varchar(255) not null,total_copies int,available_copies int)""")

    book_id=int(input("Enter the book id: "))
    Title=input("Enter the title of the book: ")
    Author=input("Enter the name of the author: ")
    total_copies=int(input("Enter the total number of copies: "))
    available_copies=int(input("Enter the number of available copies: "))

    sql=("Insert Into Books(book_id,Title,Author,total_copies,available_copies)Values(%s,%s,%s,%s,%s)")
    values=(book_id,Title,Author,total_copies,available_copies)
    cursor.execute(sql,values)

    db.commit()
    print("Book details added!")

    cursor.close()
    db.close()