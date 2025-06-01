def main():
    current_score = get_valid_score()

    menu_text = """\nOptions Menu:
(A)ssign a new valid score (0-100 inclusive)
(R)esult - Display grade
(S)how stars as score representation
(E)xit program"""

    user_choice = get_menu_choice(menu_text)

    while user_choice != "E":
        if user_choice == "A":
            current_score = get_valid_score()
        elif user_choice == "R":
            grade = determine_grade(current_score)
            print(f"Grade: {grade}")
        elif user_choice == "S":
            display_stars(current_score)
        else:
            print("Invalid selection, please choose a valid option.")

        user_choice = get_menu_choice(menu_text)

    print("Goodbye!")


def get_menu_choice(menu_text):
    print(menu_text)
    selection = input("Select an option: ").strip().upper()
    return selection


def get_valid_score():
    score_input = float(input("Enter a score between 0 and 100: "))
    while score_input < 0 or score_input > 100:
        print("Invalid input. Score must be between 0 and 100.")
        score_input = float(input("Enter a score between 0 and 100: "))
    return score_input


def determine_grade(score_value):
    if score_value >= 90:
        return "Excellent"
    elif score_value >= 50:
        return "Passable"
    else:
        return "Bad"


def display_stars(score_value):
    print("*" * int(score_value))


# Run the main program
main()
