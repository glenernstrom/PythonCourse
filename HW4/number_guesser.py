"""
Glen Ernstrom
CS 1210
July 25, 2026

A number guessing game.
"""

import random  # Don't change or remove this line!

MAX_GUESSES = 10  # Don't change or remove this line!
UPPER_BOUND = 2**MAX_GUESSES  # Don't change or remove this line!


def get_guess(guesses):
    """
    This function is responsible for getting a valid guess from the user.
    It should take a list of guesses as an argument, and gets a new, valid
    guess from the user. It should first report the number of guesses remaining.
    Then it should prompt for a guess, and validate user input making sure that
        1) the user's guess in in the interval [1, UPPER_BOUND], and
        2) the user hasn't already guessed that number.
    The function should only return once a valid guess has been made and this
    has been appended to the list of guesses.
    """
    while True:
        print(f"You have {MAX_GUESSES - len(guesses)} remaining.")
        guess = int(input("Enter your guess: "))
        if (guess < 1) or (guess > UPPER_BOUND):
            print(f"INVALID! Must be in the interval [1, {UPPER_BOUND}]. Try again.")
        elif guess in (guesses):
            print("INVALID! You've already guessed that. Try again.")
        else:
            guesses.append(guess)
            return guess


def check_guess(guess, secret_number):
    """
    This function is responsible for checking if a guess is correct,
    and reporting whether high or low if incorrect. It should take two
    arguments, a guess and a secret number. If guess equals the secret
    number it should print "CORRECT!" and return True. If the guess is too
    low, it should print "Guess is too LOW!" and return False. If the guess
    is too high it should print "Guess is too high!" and return False.
    """
    if guess > secret_number:
        print("Guess is too HIGH!")
        return False
    elif guess < secret_number:
        print("Guess is too LOW!")
        return False
    else:
        guess = secret_number
        print("CORRECT!")
        return True


def play(secret_number):
    """
    This function runs the game. We start with an empty list of guesses and
    a variable `win`, initially set to False. Then, as long as there are
    guesses remaining, it should call get_guess() to get a new guess and
    check_guess() to check if a guess is correct. If the user's guess is
    correct, the game is over, and this function should report the win,
    the secret number and the number of guesses it took to guess correctly.
    If the user runs out of guesses, the function should report the loss
    and the secret number.
    """

    print(f"Try to guess the secret number from 1 to {UPPER_BOUND}.")
    guesses = []  # Don't change or remove this line!
    win = False  # Don't change or remove this line!

    while win == False:
        guess = get_guess(guesses)
        win = check_guess(guess, secret_number)
        if win == True:
            print(
                f"You WIN! The secret number was {secret_number} and it took you {len(guesses)} guesses."
            )
        elif len(guesses) == MAX_GUESSES:
            print(f"You LOSE! The secret number was {secret_number}.")
            break


if __name__ == "__main__":
    secret_number = random.randint(1, UPPER_BOUND)  # Replace None with a random number
    play(secret_number)  # Don't change or remove this line!
