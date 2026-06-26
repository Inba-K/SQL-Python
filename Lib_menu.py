import Library
import Library1
import Library3
import Library4
import Library5
print("*"*60)
print("\tWelcome to the Fremont Public Library System!")
print("*"*60)
while True:
    print("Menu 1: Librarian's book entering system.")
    print("Menu 2: Student registration.")
    print("Menu 3: Librarian's restocking system.")
    print("Menu 4: Book issuing system.")
    print("Menu 5: View the books.")
    a=int(input('Enter the menu you want to see: '))
    if a==1:
        Library.Menu_1()
    elif a==2:
        Library1.Menu_2()
    elif a==3:
        Library3.Menu_3()
    elif a==4:
        Library4.Menu_4()
    elif a==5:
        Library5.Menu_5()
    else:
        break