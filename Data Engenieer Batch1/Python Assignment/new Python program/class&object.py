
# creating a class and a object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

    # Create a new instance of the Person class and assign it to the variable person1


person1=Person("Kanak",22)
person1.greet()