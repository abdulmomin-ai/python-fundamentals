from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance   # Private variable
        
# Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Deposit must be positive")
            
# Withdraw Method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Withdraw Unsuccessfull: Insufficient Fund")
# Get Balance
    def get_balance(self):
        return self.__balance
    
# abstract method
    def account_type(self):
        pass
    
# Implementation of Abstarct Method
class SavingAccount(Account):
    def account_type(self):
        return "Saving"
    
    def calculate_interest(self, rate=0.05):
        return self.get_balance() * rate
    
# File Handling System     
def save_account(account):
    with open("accounts.txt", "w") as file:
        for acc in account:
            file.write(f"{acc.name},{acc.get_balance()},{acc.account_type()}")
            
            

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

def admin_panel(accounts):
    print("\n=== ALL ACCOUNTS ===")
    for acc in accounts:
        print(f"Name:{acc.name}, Balance:{acc.get_balance()}, Type:{acc.account_type()}")

def main():
    accounts = load_accounts()

    while True:
        print("\n=== BANK MANAGEMENT SYSTEM ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Calculate Interest")
        print("6. Admin Panel")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            balance = float(input("Enter Initial Balance: "))
            account = SavingAccount(name, balance)
            accounts.append(account)
            
            print("Account created successfully.")
            

        elif choice == "2":
            name = input("Enter Name: ")
            for acc in accounts:
                if acc.name == name:
                    amount = float(input("Enter amount to deposit: "))
                    acc.deposit(amount)
                   
                    break
            else:
                print("Account not found.")
                

        elif choice == "3":
            name = input("Enter Name: ")
            for acc in accounts:
                if acc.name == name:
                    amount = float(input("Enter amount to withdraw: "))
                    acc.withdraw(amount)
                    
                    break
            else:
                print("Account not found.")
                

        elif choice == "9":
            name = input("Enter Name: ")
            for acc in accounts:
                if acc.name == name:
                    print(f"Balance: {acc.get_balance()}")
                    break
            else:
                print("Account not found.")
                

        elif choice == "5":
            name = input("Enter Name: ")
            for acc in accounts:
                if acc.name == name:
                    interest = acc.calculate_interest()
                    print(f"Interest on current balance: {interest}")
                    break
            else:
                print("Account not found.")

        elif choice == "6":
            admin_panel(accounts)

        elif choice == "7":
            print("Thank you for using the Bank Management System.")
            break

if __name__ == "__main__":
    main()








                




