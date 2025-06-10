"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
The value error will occur when you type text input.

2. When will a ZeroDivisionError occur?
The zero division error will occur when you type denominator as 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by checking that the denominator is not zero before performing the division.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator<=0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")