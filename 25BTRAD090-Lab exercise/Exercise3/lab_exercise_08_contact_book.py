# Lab Exercise 8: Contact Book Using Lists and Dictionaries
# Student: Rithik Roshan | USN: 25BTRAD090
#CONTACT BOOK
contacts = []  # This list will hold all the contacts


def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter their phone number: ")
    email = input("Enter their email: ")

    # Store one person's details together
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added.")


def find_contact(name):
    # Look through the list until we find a matching name
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return None  # Return this if no contact matches


def search_contact():
    name = input("Who are you looking for? ")
    contact = find_contact(name)

    if contact:
        print(contact)
    else:
        print("Contact not found.")


def update_contact():
    name = input("Which contact do you want to update? ")
    contact = find_contact(name)

    if contact:
        contact["phone"] = input("Enter the new phone number: ")
        contact["email"] = input("Enter the new email: ")
        print("Contact updated.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Which contact do you want to delete? ")
    contact = find_contact(name)

    if contact:
        contacts.remove(contact)
        print("Contact deleted.")
    else:
        print("Contact not found.")


def display_contacts():
    if not contacts:
        print("The contact book is empty.")
        return

    for contact in contacts:
        print(contact)
# Keep showing the menu until the user chooses to quit
while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 6.")

