# Lab Exercise 5: Number Guessing Game
# Student: Rithik Roshan | USN: 25BTRAD090
import random

n = random.randint(1, 10)

g = int(input("Guess a number between 1 and 10: "))

if g == n:
    print("Correct guess!")
else:
    print("Wrong guess!")
    print("The number was", n)
