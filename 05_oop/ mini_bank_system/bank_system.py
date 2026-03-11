from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance      # Private Variable 

# Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            

# Withdraw Method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Successfull:")
        else:
            print("Insufficient Amount. Withdraw Unsuccessfull")

# Get Balance
    def get_balance(self):
        return self.__balance
    
    @abstractmethod
    def account_type(self):
        pass

# Implementation of Abstarct Method
class SavingAccount(Account):
    def account_type(self):
        return "Saving"
    
 # File Handling System 
def save_account(account):
    with open("accounts.txt", "a") as file:
       file.write(f"{account.name},{account.get_balance()},{account.account_type()}\n")

def load_accounts():
    accounts = []

    try:
         with open("accounts.txt", "r") as file:
             for line in file:
                 name, balance, account_type = line.strip().split(",")
                 if account_type == "Saving":
                   accounts.append(SavingAccount(name, float(balance)))
    except FileNotFoundError:
         pass
    return accounts
    
def main():
    accounts = load_accounts()

    while True:
         print("\n1. Create Account:")
         print("2. Deposit")
         print("3. Withdraw")
         print("4. Check Balance")
         print("5. Exit")

         choice = input("Enter your Choice: ")

         if choice == "1":
            name = input("Enter your Name:")
            balance = float(input("Enter your initial Balance: "))
            account = SavingAccount(name, balance)
            accounts.append(account)
            save_account(account)
            print("Account Created Successfully")

         elif choice == "2":
                name = input("Enter your Name:")
                for acc in accounts:
                  if acc.name == name:
                    amount = float(input("Enter Amount:"))
                    acc.deposit(amount)
                    print("Amount Deposited")

         elif choice == "3":
                name = input("Enter your Name: ")
                for acc in accounts:
                  if acc.name == name:
                     amount = float(input("Enter Amount: "))
                     acc.withdraw(amount)
                    
                     

         elif choice == "4":
               name = input("Enter Name: ")
               for acc in accounts:  
                 if acc.name == name:
                    print("Balance", acc.get_balance())

         elif choice == "5":
               print("Program closed")
               break

if __name__ == "__main__":
    main()
    
    




        
      













      