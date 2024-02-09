# Constructor

class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def emp_details(self):
        print("Employee Id: ", self.id)
        print("Employee Name: ", self.name)
        print("Employee Salary: ", self.salary)
        print("\n")

emp1 = Employee(1,"Kanak",50000)
emp2 = Employee(2,"Anushka",70000)
emp3 = Employee(3,"Dhruv",100000)

emp1.emp_details()
emp2.emp_details()
emp3.emp_details()