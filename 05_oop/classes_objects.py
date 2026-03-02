# Basic Class and Method
class Person:
    def speak(self):
        print("Person can speak")
p1 = Person()
p1.speak()



#  Multiple Objects of Same Class
class Person:
    def speak(self):
        print("Hello!")
p1 = Person()
p2 = Person()    # Object Creation

p1.speak()      # Object calling function
p2.speak()



# Class with Data
class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person()
p1.set_data("Momin", 20)
p1.show_data()

p2 = Person()
p2.set_data("Ahmed", 25)
p2.show_data()



# Car Class Example
class car:
    def set_info(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(self.brand, "is driving at", self.speed, "km/h")
car1 = car()
car1.set_info("Honda Civic RS", 190)
car1.drive()



# Mobile Class Example
class Mobile:
    def set_specs(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def show_specs(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram,)

m1 = Mobile()
m1.set_specs("iPhone", "8 GB")
m1.show_specs()



#  Student Class Example
class Student:
    def set_details(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa

    def display(self):
       # print(self.name, self.roll_no, self.cgpa)
         print("Name:", self.name)
         print("Roll Num:", self.roll_no)
         print("CGPA:", self.cgpa)

s1 = Student()
s1.set_details("Abdul Momin", 228, 3.8)
s1.display()
# self : Reference of current Object



# Bank Customer Task
class BankCustomer:
    def set_data(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Name:", self.name, "Balance:", self.balance)


c1 = BankCustomer()
c1.set_data("Ali", 50000)
c1.show_balance()



