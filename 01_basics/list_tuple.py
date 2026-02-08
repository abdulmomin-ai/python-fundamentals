# List Basics

numbers = [1, 3, 5, 7, 9]
print(numbers[0])


# Lists are chnageable so you can update the value within the list
numbers = [3, 6, 9]
numbers[1] = 100
print(numbers)


# Adding elements to list
fruits = ["apple", "Guava", "watermelon"]
fruits.append("Mango")       # add at last
fruits.insert(1, "Grapes")   # add at mentioned position
print(fruits)

 

# Removing elements from list
item = [1, 23, 42, 57, 20]
item.remove(23)  # remove mentioned number
item.pop()       # remove last element
item.pop(2)      # remove mentioned index number
print(item)


# Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[:-3])   # 10 20 30



# Sorting and reversing
marks = [23, 56, 12, 8, 11]
marks.sort()    # sorting
print("Ascending order:", marks)
marks.sort(reverse=True)   # reverse
print("Descending order:", marks)



# List with user inpput
marks = []
for i in range(5):
 num = int(input("Enter any number: "))
 marks.append(num)
print("All makrs", marks)
print("Highest", max(marks))
print("Avg", sum(marks)/len(marks)) 



# Simple mini use case
cart = []
while True:
    item = input("Enter any items: ")
    if item == "done":
      break
    cart.append(item)
print("All items", cart)




# Tuple Examples


student = ("Abdul", 21, "Pakistani")
print(student[0])
print(student[1])


# Tuple unpacking
person = ("Momin", 20, "Pakistani")
name, age, nationality = person
print(name, age, nationality)



# Practical List operations
nums = []
for i in range(5):
    x = int(input("Enter number: "))
    nums.append(x)
print("Even numbers:")
for n in nums:
    if n % 2 == 0:
        print(n)















