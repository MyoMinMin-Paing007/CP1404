"""CP1404 prac"""

usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
]

username = input("Enter your username: ")

# Check if the entered username is in the list
while username not in usernames:
    print("Access denied!")
    username = input("Enter your username: ")

print("Access granted!")
