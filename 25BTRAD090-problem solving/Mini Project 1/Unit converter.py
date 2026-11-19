#Mini Project Unit converter
print("Unit Converter")

print("1. Meter to Centimeter")
print("2. Kilometer to Meter")


choice = int(input("Enter your choice: "))
v = float(input("Enter value: "))

if choice == 1:
    result = v * 100
    print("Result =", result, "centimeters")
    
elif choise == 2:
    result = v* 1000
    print("Result =", result, "meters")


