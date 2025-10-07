# Mini-Project: Number Guessing Game
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = 0

print("I'm thinking of a number between 1 and 100.")

while guess != secret_number:
    guess_str = input("What's your guess? ")

    # Check if the input is a number
    if not guess_str.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess_str)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You got it! The number was " + str(secret_number))