"""CP1404 prac"""

import random

# Constants
NUMBERS_IN_PICK = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45

def main():
    try:
        total_quick_picks = int(input("How many quick picks? "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    for _ in range(total_quick_picks):
        pick_numbers = create_quick_pick()
        print(" ".join(f"{number:2}" for number in pick_numbers))

def create_quick_pick():
    quick_pick_numbers = []
    while len(quick_pick_numbers) < NUMBERS_IN_PICK:
        random_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        if random_number not in quick_pick_numbers:
            quick_pick_numbers.append(random_number)
    quick_pick_numbers.sort()
    return quick_pick_numbers

if __name__ == "__main__":
    main()
