#for variable in iterable
for i in range(1 , 5):
    print(i)


# Print even numbers from 0 to 20
for i in range(0 , 21, 2):
    print(i)
 
 
# Print name 5 times 
for i in range(5):
    print("Abdul momin")
    
    
# Countdown from 10 to 1
for i in range(10, 0 , -1):
 print(i)
 

# Sum of first 10 natural numbers
total = 0
for i in range(1 , 11):
    total += i
    print("Total:", total)
    


# Multiplication table for a number
num = int(input("Enter any number"))

for i in range(1 , 11):
    print(num, "x", i, "=", num * i)
    

# Count vowels in a string
text = "Abdul Momin"
count = 0

for ch in text.lower():   
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)


# Reverse a string
text = "Python"
rev = ""

for ch in text:
    rev = ch + rev
    print("Revrse:", rev)
   


# Iterate over list
fruits = ["apple", "banana", "mango"]

for item in fruits:
    print(item)




# While Loops

# Print numbers 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
    


# Print even numbers 0 to 20
i = 0
while i <= 20:
    print(i)
    i += 2
    


# Countdown from 10 to 1    
i = 10
while i >= 1:
    print(i)
    i -= 1
    
# Infinite input until exit typed
while True:
  text = input("Enter text (exit to stop):")
  if text == "exit":
      break
  print("You typed:", text)



# Password verification loop
password = "12345"
attempt = ""

while attempt != password:
    attempt = input("Enter pass")
print("Access Granted")



# Sum numbers until user enters 0
total = 0
while True:
    num = int(input("Enter number (0 to stop)"))
    if  num == 0:
        break
    total += num
print("Total:", total)








    

