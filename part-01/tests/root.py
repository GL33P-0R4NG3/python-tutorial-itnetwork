#!/usr/bin/env python3

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")

a = get_number("Zadej číslo k umocnění:\n")

print(f"Výsledek: {a ** 2}")