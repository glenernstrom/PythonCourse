MAX_GUESSES = 10                 # Don't change or remove this line!
UPPER_BOUND = 2 ** MAX_GUESSES   # Don't change or remove this line!


guesses = []

while True:
    print(f"You have {MAX_GUESSES-len(guesses)} remaining.")
    guess = int(input("Enter your guess: "))
    if (guess < 1) or (guess > UPPER_BOUND):
        print (f"INVALID! Must be in the interval [1, {UPPER_BOUND}]. Try again.") 
    elif guess in (guesses):
        print("INVALID! You've already guessed that. Try again.")
    else:
        guesses.append(guess)
    print(guesses)


