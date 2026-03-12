# Using math module (Compound Interest)
import math
prinicpal = 50000
rate = 0.08
time = 2
Compound_Interest = prinicpal * math.pow((1 + rate), time)
print("Total Amount with interest: ", int(Compound_Interest))


# Using math.sqrt()
import math 
numbers = [1, 3, 5, 8]
for num in numbers:
    print("Answer", int(math.sqrt(num)))



# Using math.sqrt()
from datetime import datetime
now = datetime.now()
print("Current Date: ", now.date())
print("Current time: ", now.time().strftime("%I: %M: %S"))



# Banking Transaction log 
from datetime import datetime
def log_transaction(name, amount, action):
    time = datetime.now().strftime("%Ihr: %Mmin: %Ssec").lstrip("0")
    print(f"{time} | {name} | {amount} | {action}")
log_transaction("Abdul Momin", "90,000", "Deposit")



# Create Folder 
import os 
folder_name = "bank_reports"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder Created Successfully")
else:
    print("Folder Already Exists")



# Save file inside folder
import os
folder = "bank_reports"

if not os.path.exists(folder):
    os.mkdir(folder)
file_path = os.path.join(folder, "report.txt")
with open(file_path, "w") as file:
    file.write("Bank report generated successfully")
print("Report Saved")



#  Mini Banking Report Example
import os
from datetime import datetime


class DummyAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def account_type(self):
        return "Saving"

def generate_report(accounts):
    folder = "reports"

    if not os.path.exists(folder):
        os.mkdir(folder)

    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"report_{date}.txt"

    path = os.path.join(folder, file_name)

    with open(path, "w") as file:
        file.write("NAME | BALANCE | ACCOUNT TYPE\n")
        file.write("-----------------------------\n")
        for acc in accounts:
            file.write(f"{acc.name} | {acc.get_balance()} | {acc.account_type()}\n")

    print("Report Generated Successfully")
    print("File saved at:", path)
accounts = [
    DummyAccount("Momin", 1500),
    DummyAccount("Ali", 3000)
]
generate_report(accounts)
    




