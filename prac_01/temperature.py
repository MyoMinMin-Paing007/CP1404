"""
CP1404 - Practical
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

user_input = input(">>> ").upper()

while user_input != "Q":
    if user_input == "C":
        temp_celsius = float(input("Celsius: "))
        temp_fahrenheit = temp_celsius * 9.0 / 5 + 32
        print(f"Result: {temp_fahrenheit:.2f} F")

    elif user_input == "F":
        temp_fahrenheit = float(input("Fahrenheit: "))
        temp_celsius = 5 / 9 * (temp_fahrenheit - 32)
        print(f"Result: {temp_celsius:.2f} C")

    else:
        print("Invalid option")

    print(MENU)
    user_input = input(">>> ").upper()

print("Thank you.")