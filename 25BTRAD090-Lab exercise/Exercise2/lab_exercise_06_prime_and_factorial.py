# Lab Exercise 6: Prime Number and Factorial Programs
# Student: Rithik Roshan | USN: 25BTRAD090
#Prime Number
x = int(input("Enter a number: "))

if x < 2:
    print("Not a Prime Number")
else:
    for i in range(2, x):
        if x % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
#Factorial

n = int(input("Enter a number: "))
a = 1

for i in range(1, n + 1):
    a= a* i

print("Factorial =", a)
