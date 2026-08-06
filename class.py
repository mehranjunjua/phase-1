
"""
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Course : ", self.course)

    def study(self):
        print(self.name, "is studying", self.course)


student1 = Student("Hamza", 20, "Python")
student2 = Student("Azeem", 23, "FastAPI")

student1.display()
student1.study()

print("-------------------")

student2.display()
student2.study()

print("-------------------")

student3 = Student("Mehran","29","Backend Development")

student3.display()
student3.study()

"""

class mobile: 

     def __init__(self):
          self.__price = 0 

     def setprice(self, price):
          self.__price += price
          print("Then enterd price is =  ", self.__price)

     def getprice(self):
          pric = int(input("Please enter any price =  "))
          self.__price = pric
          print("Then enterd price is =  ", self.__price)           



m1 = mobile()

m1.setprice(300)
m1.getprice()
