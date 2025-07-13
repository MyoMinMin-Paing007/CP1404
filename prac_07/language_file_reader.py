"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
Updated to include pointer arithmetic support
"""

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    in_file = open('languages.csv', 'r')
    in_file.readline()  # Skip header

    for line in in_file:
        parts = line.strip().split(',')
        if len(parts) != 5:
            continue  # skip malformed or blank lines
        name, typing, reflection_str, year_str, pointer_str = parts
        reflection = reflection_str == "True"
        pointer_arithmetic = pointer_str == "True"
        year = int(year_str)

        language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
        languages.append(language)

    in_file.close()

    for language in languages:
        print(language)


if __name__ == '__main__':
    main()
