# Opening and closing a file
file = open("example.txt", "w")  
file.write("Hello World!\n")    
file.close()                     


# Reading a file
file = open("example.txt", "r")
data = file.read()
file.close()
print("File Content:\n", data)


# Reading Line By Line
file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()


# Writing user input to file
name = input("Enter your name:")
age = input("Enter your age:")
city = input("Enter your city:")

file = open("user.txt", "w")
file.write(f"Name:, {name}\n")
file.write(f"Age:, {age}\n")
file.write(f"City:, {city}\n")
file.close()
print("Data save successfully")


# Reading user data from file
file = open("user.txt", "r")
data = file.read()
file.close()
print("File Content\n", data)


# Writing List of Dictionaries to file
users = [
    {"name":"Momin", "age":20, "CGPA":"3.5"},
    {"name":"Ahmad", "age":23, "CGPA":"3.7"},
    {"name":"Adnan", "age":25, "CGPA":"3.8"}
     ]
file = open("student.info", "w")
for u in users:
    file.write(f"Name: {u['name']}, Age: {u['age']}, CGPA: {u['CGPA']}\n")
file.close()








