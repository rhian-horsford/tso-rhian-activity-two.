"""Two guessing games: find the computer's number, or reveal a hidden GitHub term."""

import random

LOW = 1
HIGH = 100

WORDS = [
    "repository",
    "repo",
    "commit",
    "branch",
    "switch",
    "clone",
    "remote",
    "origin",
    "pull",
    "push",
    "merge",
    "tag",
    "pull request",
]

MAX_WRONG = 6


def play_number():
    secret = random.randint(LOW, HIGH)
    attempts = 0

    print(f"\nI'm thinking of a number between {LOW} and {HIGH}. Can you find it?")

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


def _masked(word, guessed):
    return " ".join(c if c == " " or c in guessed else "_" for c in word)


def _normalize(text):
    return " ".join(text.lower().split())


def play_word():
    word = random.choice(WORDS)
    letters = {c for c in word if c != " "}
    guessed = set()
    wrong = 0

    print("\nI'm thinking of a GitHub term. Guess it one letter at a time.")
    if " " in word:
        print("Heads up: this one is two words.")

    while True:
        print(f"\n{_masked(word, guessed)}    ({MAX_WRONG - wrong} misses left)")
        entry = input("Guess a letter, or '!' to guess the whole term: ").strip().lower()

        if entry == "!":
            attempt = input("Enter the full term (blank to cancel): ").strip()
            if not attempt:
                continue
            if _normalize(attempt) == word:
                print(f"\nSpot on: {word}!")
                return
            wrong += 1
            if wrong >= MAX_WRONG:
                print(f"\nOut of guesses. The term was '{word}'.")
                return
            print("That's not it. Costs you a miss.")
            continue

        if len(entry) != 1 or not entry.isalpha():
            print("Please enter a single letter, or '!' to guess the whole term.")
            continue

        if entry in guessed:
            print(f"You already tried '{entry}' - no penalty, pick another.")
            continue

        guessed.add(entry)

        if entry in letters:
            if letters <= guessed:
                print(f"\nYou got it: {word}!")
                return
            print("Yes!")
        else:
            wrong += 1
            if wrong >= MAX_WRONG:
                print(f"\nOut of guesses. The term was '{word}'.")
                return
            print("Nope.")


def choose_game():
    while True:
        print("\n1) Number guessing game")
        print("2) Word guessing game (GitHub terms)")
        choice = input("Pick a game (1/2), or 'q' to quit: ").strip().lower()

        if choice == "1":
            return play_number
        if choice == "2":
            return play_word
        if choice.startswith("q"):
            return None
        print("Please enter 1, 2, or q.")


def main():
    print("Welcome! Two games to choose from.")
    try:
        while True:
            game = choose_game()
            if game is None:
                break
            game()
            again = input("\nPlay again? (y/n): ").strip().lower()
            if not again.startswith("y"):
                break
        print("Thanks for playing!")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
