# Lab Exercise 15: Library Management System
# Student: Rithik Roshan| USN: 25BTRAD090
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = [Book("Python Basics"), Book("Computer Science")]

    def show_books(self):
        for book in self.books:
            status = "Available" if book.available else "Issued"
            print(book.title, "-", status)

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print("Book issued.")
                return
        print("Book not found or already issued.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print("Book returned.")
                return
        print("That book is not currently issued.")

library = Library()

while True:
    print("\n1. Show books  2. Issue book  3. Return book  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        library.show_books()
    elif choice == "2":
        library.issue_book(input("Book title: "))
    elif choice == "3":
        library.return_book(input("Book title: "))
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
