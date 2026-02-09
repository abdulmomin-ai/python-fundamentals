# Dictionary Examples

student = {
    "name": "Abdul",
    "age": 21,
    "cgpa": 3.41
}
print(student["name"])
print(student["age"])

student["age"] = 20                     # Updating
student["nationality"] = "Pakistani"    # Adding
student.pop("cgpa")                     # Removing

print(student)



# Looping in Dcitionary
person = {"name": "Ali", "age": 20, "country": "Pakistan"}
for key in person:
    print(key, ":", person[key])
    
    


# Nested Dictionary
# useful for JSON, APIs and DATABASE OBJECTS
students = {
    1: {"name": "Momin", "age": 20, "City": "Multan"},
    2: {"name": "Zakwan", "age": 21, "City": "Lahore"}
}

print("Student 1:", students[1]["name"], students[1]["age"])
print("Student 2:", students[2]["name"])


# Creating Dictionary from Lists
keys = ["name", "age", "city"]
values = ["Abdul", 21, "Lahore"]

result = dict(zip(keys, values))
print(result)


# Practical Dictionary Use Case
employees = {
    "Ali": 50000,
    "Momin": 75000,
    "Zain": 60000
}
max_salary = max(employees.values())

for name, salary in employees.items():
    if salary == max_salary:
        print("Highest Salary:", name, "=", salary)



# Set Basics
# Sets stores unique values only

my_set = {1, 3, 4, 4, 1, 6, 6, 7, 8}
print(my_set)

q = {1, 3, 5, 3}
b = {7, 9, 3, 5}
print(q.union(b))
print(q.intersection(b))
print(q.difference(b))



# Real World set use case
# Removing duplicate emails
emails = ["momin@gmail.com", "ahmad@gmail.com", "subhan@gmail.com", "momin@gmail.com"]
unique_emails = list(set(emails))
print("Unique Emails", unique_emails)





















































