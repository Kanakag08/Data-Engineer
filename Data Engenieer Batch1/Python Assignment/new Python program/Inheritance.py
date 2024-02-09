# Inheritance

# creating a parent class
class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print(self.name, self.id)


emp = Person("Kanak", 102)  # An Object of Person
emp.Display()


# creating a child class
class Emp(Person):

    def Print(self):
        print("Emp class called")


Emp_details = Emp("Pranshi", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()


# Types of inheritance
# single inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Child class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()

# Heirrichal inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Parent class
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# child class
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# Hybrid Inheritance
class School:
    def func1(self):
        print("This function is in school.")

class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

object = Student3()
object.func1()
object.func2()