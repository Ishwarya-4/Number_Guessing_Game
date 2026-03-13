from art import logo
import random

def compare_guess(guess, answer):
    """This function is used to compare the guess and the answer and check if the answer is right!"""
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return True
    elif guess > answer:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False


def play_again():
    """This function is used to check if the user wants to play the game again"""
    play = input("Do you want to play the game again? Type 'y' or 'n': ").lower()
    if play == 'y':
        return True
    else:
        return False


def try_attempts(attempt, answer):
    """This function goes on until the attempts is 0"""
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        guess_check = compare_guess(guess, answer)
        if guess_check:
            if not play_again():
                return False
            else:
                return True
        else:
            attempt -= 1
    print("You are out of attempts!")
    return play_again()


def number_guessing_game():
    """This function starts the number guessing game"""
    print(logo)
    again = False
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    correct_number = random.randint(1,100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
        again = try_attempts(attempts, correct_number)
    elif difficulty == "hard":
        attempts =5
        again = try_attempts(attempts, correct_number)
    if again:
        print("\n" * 10)
        number_guessing_game()


number_guessing_game()