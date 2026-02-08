# List Examples

numbers = [1, 3, 5, 7, 9]
print(numbers[0])


# Lists are chnageable so you can update the value within the list

numbers = [3, 6, 9]
numbers[1] = 100
print(numbers)



fruits = ["apple", "Guava", "watermelon"]
fruits.append("Mango")       # add at last
fruits.insert(1, "Grapes")   # add at mentioned position
print(fruits)

 
 
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
print(marks)

marks.sort(reverse=True)   # reverse
print(marks)



names = ["Momin", "Zakwan", "Mughira"]
names.reverse()
print(names)




marks = []
for i in range(5):
 num = int(input("Enter any number: "))
 marks.append(num)
print("All makrs", marks)
print("Highest", max(marks))
print("Avg", sum(marks)/len(marks)) 



cart = []
while True:
    item = input("Enter any items: ")
    if item == "done":
      break
    cart.append(item)

print("All items", cart)



# Tuple Examples. It is like a list but cannot be changed.


student = ("Abdul", 21, "Pakistani")
print(student[0])
print(student[1])


person = ("Momin", 20, "Pakistani")
name, age, nationality = person
print(name, age, nationality)



num = [1, 3, 6, 7, 8]
print("First", num[0])
print("Last", num[-1])
print("Sum is", sum(num))
print("Avg is", sum(num)/len(num))



fruits = []
for i in range(5):
    f = input("Enter fruit: ")
    fruits.append(f)
print("Fruit List:", fruits)



salaries = [45000, 120000, 80000, 60000]
salaries.sort()
print("Ascending:", salaries)
salaries.sort(reverse=True)
print("Descending:", salaries)



nums = []
for i in range(5):
    x = int(input("Enter number: "))
    nums.append(x)
print("Even numbers:")
for n in nums:
    if n % 2 == 0:
        print(n)















