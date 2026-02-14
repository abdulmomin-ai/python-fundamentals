# CSV & JSON Practice Examples


# Read CSV File
import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Write CSV File
import csv

data = [
    ["Name", "Age", "City"],
    ["Momin", 20, "Berlin"],
    ["Ali", 21, "Multan"],
    ]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    


# Read CSV Using Dictionary Format
import csv
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row["Name"], row["Age"])



# Append Data to CSV
import csv

with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Momin", 18, "Berlin"])
    
    
    
# Count Students Older Than 20
import csv

count = 0
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Age"]) > 20:
            count += 1
print("Students older then 20:", count)
    
 

# Write Dictionary to JSON File
import json

student = {
    "name": "Abdul Momin",
    "Age": "20",
    "skils": ["Python", "Django"]
    }
with open("students.json", "w") as file:       
    json.dump(student, file, indent=4)
    
    
    
# Read JSON File    
import json

with open("students.json", "r") as file:
    data = json.load(file)
print(data)
print(data["name"])



# Convert Dictionary to JSON String
import json

data = {"brand": "Toyota", "year": 2023}
json_string = json.dumps(data, indent=4)
print(json_string)



# Convert JSON String to Dictionary
import json

json_txt = '{"name": "Abdul Momin:", "Age": "20 years old"}'
data = json.loads(json_txt)
print(data["name"],data["Age"])



# JSON Practical Task
import json

data = [
    {"name": "Momin", "Age": 20, "Depart": "CS 6th"},
    {"name": "Yousaf", "Age": 34, "Depart": "AI 3rd"},
    {"name": "Ali", "Age": 12, "Depart": "SE final year"}
    ]
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)
    


# Count Age ≥ 21 
import json

with open("Neha.json", "r") as file:
    students = json.load(file)    
count = sum(1 for s in students if s["Age"] >= 21)
print("Students age 21 or above:", count)

    
