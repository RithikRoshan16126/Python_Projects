#Attendance Tracker
students = {}  # Each name will be linked to their attendance records


def add_student():
    name = input("Enter the student's name: ")

    if name in students:
        print("That student is already in the list.")
    else:
        students[name] = []
        print("Student added.")


def record_attendance():
    name = input("Enter the student's name: ")

    if name not in students:
        print("Student not found. Add them first.")
        return

    status = input("Was the student present or absent? (P/A): ").upper()

    if status == "P" or status == "A":
        students[name].append(status)
        print("Attendance recorded.")
    else:
        print("Please enter P for present or A for absent.")


def show_attendance():
    if not students:
        print("There are no students yet.")
        return

    print("\nAttendance report")

    for name, records in students.items():
        total_days = len(records)
        present_days = records.count("P")

        if total_days == 0:
            percentage = 0
        else:
            percentage = (present_days / total_days) * 100

        print(
            f"{name}: {present_days} present out of {total_days} days "
            f"({percentage:.1f}%)"
        )


def find_low_attendance():
    threshold = float(input("Enter the minimum attendance percentage: "))

    print(f"\nStudents below {threshold}% attendance:")

    found_student = False

    for name, records in students.items():
        total_days = len(records)
        present_days = records.count("P")

        if total_days == 0:
            percentage = 0
        else:
            percentage = (present_days / total_days) * 100

        if percentage < threshold:
            print(f"{name}: {percentage:.1f}%")
            found_student = True

    if not found_student:
        print("No students are below that attendance level.")


# Keep showing the menu until the user chooses to quit
while True:
    print("\n1. Add student")
    print("2. Record attendance")
    print("3. Show attendance report")
    print("4. Find students below a threshold")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        record_attendance()
    elif choice == "3":
        show_attendance()
    elif choice == "4":
        find_low_attendance()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 5.")
