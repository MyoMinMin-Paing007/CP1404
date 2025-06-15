"""CP1404 prac"""
# numbers=[]
# for i in range(0,5,1):
#     number = int(input("Number:"))
#     numbers.append(number)
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# print(f"The smallest number is {min(numbers)}")
# print(f"The largest number is {max(numbers)}")
# print(f"The average of the numbers is {sum(numbers)/5}")

usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

input_username = input("Enter your username: ")

# Check if the entered username is in the list
while input_username not in usernames:
    print("Access denied!")
    input_username = input("Enter your username: ")

print("Access granted!")
