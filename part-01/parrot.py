print("Hello, I am your virtual parrot Lora, I like to repeat!")

inp = input("Tell me something: ")
out = inp + ", " + inp + "!"
print(out)

print("\n---------------------------------------------------\n")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")

a = get_number("Enter number for multiplication: ")
print(a * 2)

print("\n---------------------------------------------------\n")

print(3.14 - 2.72) # xd?

from decimal import Decimal

print(float(Decimal(3.14) - Decimal(2.72)))