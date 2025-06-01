menu_text = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(menu_text)
user_choice = input(">>> ").upper()


def convert_celsius_to_fahrenheit(celsius_temp):
    fahrenheit_result = celsius_temp * 9.0 / 5 + 32
    print(f"Result: {fahrenheit_result:.2f} F")


def convert_fahrenheit_to_celsius(fahrenheit_temp):
    celsius_result = 5 / 9 * (fahrenheit_temp - 32)
    print(f"Result: {celsius_result:.2f} C")


while user_choice != "Q":
    if user_choice == "C":
        input_celsius = float(input("Celsius: "))
        convert_celsius_to_fahrenheit(input_celsius)
    elif user_choice == "F":
        input_fahrenheit = float(input("Fahrenheit: "))
        convert_fahrenheit_to_celsius(input_fahrenheit)
    else:
        print("Invalid option")
    print(menu_text)
    user_choice = input(">>> ").upper()

print("Thank you.")
