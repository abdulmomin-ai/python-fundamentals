# Basic Inheritance Examples
# Employee and Manager
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_Employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_Manager(self):
        print("Department:", self.department)

m1 = Manager("Sawera", 50000, "Computer Science")
m1.show_Employee()
m1.show_Manager()




# Bank System
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance =  balance 

    def show_account(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

class SavingAccount(BankAccount):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest 

    def show_interest(self):
        print("Interest Rate:", self.interest)

acc = SavingAccount("Momin", 1000000, "Zero")
acc.show_account()
acc.show_interest()




# AI/Tech Company Structure
class User:
    def __init__(self, username):
        self.username = username
        

    def login(self):
        print(self.username, "Logged in")

    
class Admin(User):
    def __init__(self, username, role):
         super().__init__(username)
         self.role = role

    def access_panel(self):
         print(self.username, "has admin access")

admin1 = Admin("momin-ai", "Ai Engineer")
admin1.login()
admin1.access_panel()





# Method Overriding
class Employee:
    def role(self):
        print("Employee works for company")

class Manager(Employee):
    def role(self):
        print("Manager manages team")

m = Manager()
m.role()




# AI Platform
class user():
    def __init__(self, name):
        self.name = name

class premium_user(user):
    def use_ai_tools(self):
        print(self.name, "using ai tools")

p = premium_user("Abdul Momin")
p.use_ai_tools()
        
