import random

def main():
    user_score = int(input("Enter your score: "))
    user_result = determine_result(user_score)
    print(f"Your result is {user_result}.")

    generated_score = random.randint(0, 100)
    generated_result = determine_result(generated_score)
    print(f"Random score is {generated_score}, random result is {generated_result}.")

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
