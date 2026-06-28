grades = []

grade1 = int(input("Exam 1: "))
grades.append(grade1)

grade2 = int(input("Exam 2: "))
grades.append(grade2)

grade3 = int(input("Exam 3: "))
grades.append(grade3)

grade4 = int(input("Exam 4: "))
grades.append(grade4)

grade5 = int(input("Exam 5: "))
grades.append(grade5)

print("Highest score: ", max(grades))
print("Lowest score: " , min(grades))
print("Average score: ", sum(grades) /5)
