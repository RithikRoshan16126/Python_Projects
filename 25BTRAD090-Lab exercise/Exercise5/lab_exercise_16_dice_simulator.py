# Lab Exercise 16: Dice Simulator Using Random Module
# Student: Rithik Roshan| USN: 25BTRAD090
import random

while True:
    input("Press Enter to roll the dice (or type q to quit): ")

    # Type q at the prompt to stop
    # This second prompt keeps the example simple
    if input("Roll again? (y/n): ").lower() != "y":
        break

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print("Die 1:", die1)
    print("Die 2:", die2)
    print("Total:", die1 + die2)
