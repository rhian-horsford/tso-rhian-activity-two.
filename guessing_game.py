"""A simple number guessing game: guess the computer's number between 1 and 100."""

import random

LOW = 1
HIGH = 100


def play():
    secret = random.randint(LOW, HIGH)
    attempts = 0

    while True:
        raw = input(f"Guess a number between {LOW} and {HIGH}: ").strip()

        try:
            guess = int(raw)
        except ValueError:
            print("That's not a whole number. Try again.")
            continue

        if not LOW <= guess <= HIGH:
            print(f"Stay between {LOW} and {HIGH}, please.")
            continue

        attempts += 1

        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            plural = "" if attempts == 1 else "es"
            print(f"Correct! You got it in {attempts} guess{plural}.")
            return


def main():
    print("I'm thinking of a number. Can you find it?")
    try:
        while True:
            play()
            again = input("Play again? (y/n): ").strip().lower()
            if not again.startswith("y"):
                print("Thanks for playing!")
                return
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
