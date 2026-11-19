#Lab Exercise 12: Student Data Manager Using Files
# Student: Rithik Roshan | USN: 25BTRAD090
FILE = "students.txt"

def add_student(usn, name, gpa):
    with open(FILE, "a") as f:
        f.write(f"{usn},{name},{gpa}\n")
    print(f"Saved: {name} ({usn})")

def search_student(usn):
    with open(FILE, "r") as f:
        for line in f:
            u, n, g = line.strip().split(",")
            if u == usn:
                return f"USN: {u} | Name: {n} | GPA: {g}"
    return "Not found"

def display_all():
    print(f"\n{'USN':<14} {'Name':<16} {'GPA':<5}")
    print("-" * 38)
    with open(FILE, "r") as f:
        for line in f:
            u, n, g = line.strip().split(",")
            print(f"{u:<14} {n:<16} {g:<5}")

if __name__ == "__main__":
    open(FILE, "w").close()  # Reset file
    print("=== Student File Data Manager ===")
    add_student("25BTRAD090", "Rithik Roshan", 9.45)
    add_student("25BTRAD130", "Vishaal", 8.80)
    display_all()
    print(f"\nSearch Result: {search_student('25BTLAD001')}")
