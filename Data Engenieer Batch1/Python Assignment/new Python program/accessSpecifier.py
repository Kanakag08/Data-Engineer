# Access Specifier

# public specifier
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s = Student("John", 20)
s.display()


# private specifier
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def display_balance(self):
        print("Balance:", self.__balance)


b = BankAccount(1234567890, 5000)
b.display_balance()


# protected Modifier
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _display(self):
        print("Name:", self._name)
        print("Age:", self._age)


class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self._roll_number = roll_number

    def display(self):
        self._display()
        print("Roll Number:", self._roll_number)


s = Student("John", 20, 123)
s.display()