#!/usr/bin/env python3

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")

r = get_number("Zadej poloměr kruhu (cm):\n")
pi = 3.14

print (f"Obvod zadaného kruhu je: {2 * pi * r} cm")
print (f"Jeho obsah je {pi * r**2} cm^2")