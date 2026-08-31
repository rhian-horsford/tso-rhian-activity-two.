"""Word guessing game: reveal a hidden GitHub term one letter at a time."""

import random

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
