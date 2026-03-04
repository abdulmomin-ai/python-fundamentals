# Basic Constructor Example
class Student:
    def __init__(self, name, roll):
        self.name = name 
        self.roll = roll
    
    def display(self):
        print("Name:", self.name)
        print("Roll Num:", self.roll)

s1 = Student("Ali", 101)
s1.display()



# Car Example
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(self.brand, "Civic driving at", self.speed)


c1 = Car("Honda", 120)
c1.drive()





# Constructor with Class Variable
class Employee:
    company = "AJ Enterprises"     # class variable. same for every object

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name, self.company)
        print("Salary:", self.salary)

emp = Employee("ABDUL MOMIN", 5200)
emp1 = Employee("ZAKWAN", 5200)
emp.show_details()
emp1.show_details()




#  Example: Bank Account
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def show_details(self):
        print("Name:", self.name, "Balance is:", self.balance)


acc = Account("Momin", 20000)
acc.deposit(5000)
acc.show_details()
