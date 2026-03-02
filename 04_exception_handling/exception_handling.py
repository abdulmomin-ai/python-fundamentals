#  Basic try-except (Invalid Input Handling)
try:
    num = int(input("Enter a number:"))
    print("Number", num)
except ValueError:
    print("Invalid input! Plz enter a number")
    


# Multiple Exception Handling 
try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error, you cannot divide by a zero")
except ValueError:
    print("Enter valid input! Only Number")
except Exception as e:         # For unknown error
    print("Unknow Error", e)



# Custom Exception using raise
try:
   name = input("Enter your name:")
   if len(name) < 3:
     raise ValueError("Name tooo short")

except ValueError as e:
    print("Error:", e)
else:
    print("Name accepted")
finally:
    print("Programm completed")




# File Handling with Exception
try:
    with open("data.txt", "r") as file:
        data = file.read()
        
    with open("data.txt", "w") as file:
        file.write("Lateral raises is my fvrt exercise")
except FileNotFoundError:
    print("File not found!, Creating a new one")
    with open("data.txt", "w") as file:
        file.write("This is a new file")
        
        
   

# Task 1
try:
    username = input("Enter a username:")
    password = input("Enter a password:")
    
    if username == "" or password == "":
        raise ValueError("Fields can not be empty")
    print("Login Successfully!")
    
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("unknown error:", e)




# Task 2
try:
    a = int(input("Enter first number:"))
    b = float(input("Enter second number:"))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Number cannot be divided by zero")
except ValueError:
    print("Error: It must be a Number")




# Reusable Safe Input Function
def safe_input(message):
    try:
        return int(input(message))
    except:
        print("Error: Plz enter a valid number")
        return None
num = safe_input("Enter a age:")
print("You Age is", num)

    