# Lab Exercise 11: Log File Reader Program
# Student: Rithik Roshan| USN: 25BTRAD090

import json
from pathlib import Path

FILE = Path("students.json")

def load_students():
    if not FILE.exists():
        return []
    try:
        return json.loads(FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def save_students(students):
    FILE.write_text(json.dumps(students, indent=2), encoding="utf-8")

def find_student(students, student_id):
    return next((s for s in students if s["id"] == student_id), None)

def main():
    students = load_students()

    while True:
        print("\n1 Add  2 Search  3 Update  4 Display  5 Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            if find_student(students, student_id):
                print("That ID already exists.")
                continue
            students.append({
                "id": student_id,
                "name": input("Name: ").strip(),
                "course": input("Course: ").strip()
            })
            save_students(students)

        elif choice == "2":
            student = find_student(students, input("Student ID: ").strip())
            print(student if student else "Student not found.")

        elif choice == "3":
            student = find_student(students, input("Student ID: ").strip())
            if student:
                student["name"] = input("New name: ").strip()
                student["course"] = input("New course: ").strip()
                save_students(students)
                print("Record updated.")
            else:
                print("Student not found.")

        elif choice == "4":
            for student in students:
                print(student)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
