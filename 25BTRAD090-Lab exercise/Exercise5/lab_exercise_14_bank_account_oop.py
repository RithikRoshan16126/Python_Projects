# Lab Exercise 14: Bank Account System Using OOP
# Student: Rithik Roshan| USN: 25BTRAD090
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposit successful.")
        else:
            print("Enter an amount greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter an amount greater than zero.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print("Withdrawal successful.")

    def show_balance(self):
        print(f"Balance: {self._balance:.2f}")


account = BankAccount(input("Account holder name: "), 1000)

while True:
    print("\n1. Deposit  2. Withdraw  3. Check balance  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        account.deposit(float(input("Amount: ")))
    elif choice == "2":
        account.withdraw(float(input("Amount: ")))
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
