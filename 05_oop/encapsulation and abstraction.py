#  Encapsulation (private variables)
#  Abstraction using Abstract Base Classes


# Encapsulation Examples
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Variable

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_deposit(self):
        return self.__balance

acc = BankAccount(50000)
acc.deposit(10000) 
print(acc.get_deposit())



# Real Banking Logic
class BankkAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Successfull: Thank youu for using our service.")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Account Holder:", self.name) 
        print("Remaining Balance:", self.__balance)
              
accc = BankkAccount("Momin", 40000)
accc.withdraw(5000)
accc.show_balance()



# Abstract Method: To enforce method implementation in child classes ... No object for abstract class
from abc import ABC, abstractmethod

class Payment(ABC):
    def pay(self):
        pass
    
class CardPayment(Payment):
    def pay(self):
        print("Paid using card")
        
class CashPayment(Payment):
    def pay(self):
        print("Paid using cash")
        
pay = [CardPayment(), CashPayment()]
for l in pay:
    l.pay()



# Encapsulation and Abstraction
from abc import ABC, abstractmethod

class Acccount(ABC):
    def __init__(self, balance):
        self.__balance = balance

    def cal_interest(self):
        pass
   
    def get_balance(self):
        return self.__balance
    
class SavingAccount(Acccount):
    def cal_interest(self):
        return self.get_balance() * 0.05
    
acc = SavingAccount(15000)
print("Total Interest:", acc.cal_interest())



# Secure bank Account
class MeezanBank:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
         self.__balance += amount
         print("Amount deposited:", self.__balance)
        
    

    def withdraw(self, amount):
        if amount <= self.__balance:
             self.__balance -= amount
             print("Amount Withdraw:", self.__balance)

    def show_balance(self):
        print("Final balance:", self.__balance)
        
    
account = MeezanBank(35000)
account.deposit(5000)
account.withdraw(10000)
account.show_balance()



# Notification System
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email
    def send(self, message):
        print(f"Sending Email to {self.email}: {message}")

       
class PushNotification(Notification):
    def __init__(self, device_id):
        self.device_id = device_id
    def send(self, message):
        print(f"Sending push to {self.device_id}: {message}")
    

noti = [EmailNotification("momin@gmail.com"), PushNotification("Device123")]
for s in noti:
    s.send("Hello User")
