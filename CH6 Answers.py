#Problem 1
import csv

with open('students.csv', mode='r', newline='', encoding='cp1252') as file:
    reader = csv.DictReader(file)
    print("Students who scored above 80:")
    
    for row in reader:
        grade = int(row['Grade'])
        if grade > 80:
            print(row['Name'])

#Problem 2
import json

data = {"course": "Python", "duration": "3 months", "students": ["Ali", "Sara"]}

with open('course.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

with open('course.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

print("Students:", loaded_data["students"])

#Problem 3
import pandas as pd

employees = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ali", "Mona", "Omar"],
    "Salary": [5000, 6000, 5500]
})
employees.to_excel("employees.xlsx", index=False)
df = pd.read_excel("employees.xlsx")
print(df[["Name", "Salary"]])

#Problem 4
import csv
import json

def csv_to_json(csv_file, json_file):
    people_list = []
    
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            people_list.append({
                "Name": row["Name"],
                "Age": int(row["Age"]),
                "City": row["City"]
            })
    
    data = {"people": people_list}
    
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

csv_to_json("people.csv", "people.json")