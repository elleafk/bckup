#Exercise 1
animals = ["Dog", "Cat", "Bird", "Fish"]

for animal in animals:
    print(animal)
    
#Exercise 2
for number in range(1,6):
    print(number)
    
#Exercise 3
subjects = ["Python", "Math", "Science", "English"]

for number,subject in enumerate(subjects, start=1):
    print(number,subject)
    
#Exercise 4
students = ["Anna", "Ben", "Cara"]
grades = [95,88,91]

for student,grade in zip(students, grades):
    print(student, " got ", grade)
    
#Exercise 5
grades = [95,82,76,91,68]

for grade in grades:
    if grade >=75:
        print(grade, " Passed")
    else:
        print(grade, " Failed")
    
#Exercise 6
tasks = []

for i in range(1,4):
    task = input(f"Task {i}: ")
    tasks.append(task)
    
print("My Tasks:")
for task in tasks:
    print(task)
    
#Exercise 7
names = ["Anna", "Ben", "Cara"]
scores = [90,75,98]

for num, (name,score) in enumerate(zip(names, scores), start=1):
    print(num, name, " scored ", score)
    
#Exercise 8
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [50000,800,1500,7000]

print("==== PRICE LIST ====")
for number, (product,price) in enumerate(zip(products,prices), start=1):
    print(number, product, " - ", price)
print("====================")


















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
