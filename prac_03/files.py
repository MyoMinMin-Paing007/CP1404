"""
CP1404 Practical - Suggested Solution
Make the appropriate choice of file-reading technique for each of these questions:
- read()
- readline()
- readlines()
- for line in file
"""

# 1st program
# Open a file to write the user's name
# Use print to write the name into the file
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2nd program
# Open the file and read the whole text from file
# strip() removes any extra whitespace or newline characters
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3rd program
# Read two numbers from a file, using readline() to get one line at a time
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4th program
# Loop through the file to read and add up all numbers
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
