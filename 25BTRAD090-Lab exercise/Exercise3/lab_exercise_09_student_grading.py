# Lab Exercise 9: Student Grading System
# Student: Rithik Roshan| USN: 25BTRAD090
#Student grading system
students = {}  # Each student's name will be linked to their mark
# Ask how many student records to enter
number_of_students = int(input("How many students are there? "))

for _ in range(number_of_students):
    name = input("Enter the student's name: ")
    mark = float(input("Enter their mark out of 100: "))

    students[name] = mark


print("\nStudent results:")

# Work out a grade for each student's mark
for name, mark in students.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: {mark} marks — Grade {grade}")
