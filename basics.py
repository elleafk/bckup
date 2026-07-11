#List
names = []

students = int(input("How many students do you want to enter? "))

for i in range(students):
student = input(f"Enter student name {i+1}: ")
names.append(student)

print("Total number of students: ",students, "\n")
print("List of students name: ")

for num, name in enumerate(names, start=1):
print(num, name)

#Tuple

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print("Months of the year")
for num, month in enumerate(months, start=1):
print(num, month)

#Sets
colors = {"Purple", "Red", "Yellow", "Red"}

for num, color in enumerate(colors, start=1):
print(num, color)

colors.add("Blue")

print("\n")
for num,color in enumerate(colors, start=1):
print(num, color)

colors.remove("Purple")

print("\n")
for num, color in enumerate(colors, start=1):
print(num, color)

#Dictionaries
studInfo = {
"name": "Janelle",
"age": 19,
"course": "BSIT"
}

print(studInfo["name"])
studInfo["age"] = 20

studInfo["school"] = "BulSU"

print(studInfo)

#functions
name = input("What is your name? " )

def greetings(name):
print("Hello ", name,"!")

greetings(name)

#modules
import datetime

print(datetime.datetime.now())
