
"""
def writing():
 while True:
      name = input("Enter Name: " )
      age = int(input("Enter age:  "))
      course = input("Enter Course: ")
      file = open("clistu.txt", "a")
      file.write(f"{name},{age},{course}\n")
      file.close()
      break

def read():
 while True:
      file = open("clistu.txt", "r")
      print(file.read())
      file.close()
      break


def search():
  sname = input("Enter name which you want to search :   ")
  with open("clistu.txt", "r") as file:
  data = file.read()
  if  sname  in data:
        print("Student found: ")
  else:
        print("Student Not Found :  ")
        


def delete():

   dname = input("Enter name which you want to delete :   ")
   with open("clistu.txt", "r") as file:
   dfind = file.read()
   if dname == dfind:
       pop(dfind)
   else:
       print("Student Not Found :  ")


"""


def add_student():
    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        with open("students.txt", "a") as file:
            file.write(f"{name},{age},{course}\n")

        print("Student Added Successfully!")

    except ValueError:
        print("Age must be a number.")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.read()

            if data == "":
                print("No Records Found.")
            else:
                print("\n===== Student Records =====")
                print(data)

    except FileNotFoundError:
        print("No student file found.")


def search_student():
    try:
        search_name = input("Enter student name: ")

        found = False

        with open("students.txt", "r") as file:
            for line in file:
                if search_name.lower() in line.lower():
                    print(line.strip())
                    found = True

        if not found:
            print("Student Not Found.")

    except FileNotFoundError:
        print("No student file found.")


def delete_student():
    try:
        delete_name = input("Enter student name to delete: ")

        found = False

        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                if delete_name.lower() not in line.lower():
                    file.write(line)
                else:
                    found = True

        if found:
            print("Student Deleted Successfully.")
        else:
            print("Student Not Found.")

    except FileNotFoundError:
        print("No student file found.")