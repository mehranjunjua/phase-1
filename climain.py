"""
from clistu import *

while True:
    print("\n, if you want to write new record for student press : 1 , for read press : 2, for search : 3, for delete press :4 ")
    xyz = int(input("Enter your choice = "))
    if xyz == 1:
        writing()
    elif xyz == 2:
        read()
    elif xyz == 3:
        search()
    elif xyz == 4:
        delete()
    else:
        print("You enter invlid number")
        break

"""


from student import *

while True:

    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            delete_student()

        elif choice == 5:
            print("Thank you!")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid number.")