# Basic Python Funtions


def greet():
    print("Hello world!")  
greet()


# Function with parameter
def user(name):
    return f"Hey {name}! Welcome to Python"
    
print(user("Abdul Momin"))


# Function to add two numbers
def add(a, b):
    return a + b

sum = add(5, 6)
print("Sum is", sum)


# Sum() Function
def sum(x, y):
 return x + y

a = int(input("Enter any num:"))
b = int(input("Enter any num:"))

total = sum(a, b)
print("Answer is", total)


# Factorial using function
def factorial(n):
   result = 1
   for i in range(1, n+1):
       result *= i     
   return result
    
num = int(input("Enter any number to find factorial"))
fact = factorial(num)
print("factorial of",num,"is", fact)


#BMI Calculator
def cal_bmi(weight, height):
  height_m = height / 100    # cm → meters
  bmi = weight / (height_m ** 2)
  return bmi

a = float(input("Enter your weight in kg: "))
b = float(input("Enter your height in cm: "))

BMI = cal_bmi(a, b)
print("Your bmi value is", round(BMI, 2))

if BMI >= 20 and BMI < 25:
   print("Normal")
elif BMI >= 25:
   print("Obese")
else:
    print("You are skinny")


# Return Square
def cal_sq(num):
    return num * num

number = int(input("Enter any number to find square: "))
result = cal_sq(number)
print("Sqaure of this Number is", result)


# Even odd Check
def even(num):
  if num % 2 == 0:
      return True
  else:
      return False
    
number = int(input("Enter any number: "))
if even(number):
    print(number, "is even")
else:
    print(number, "is odd")


# Calculator
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, op)
print("Result:", result)















