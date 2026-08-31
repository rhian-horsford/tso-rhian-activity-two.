"""Entry point: pick one of the three games."""

from adventure import play_adventure
from number_game import play_number
from word_game import play_word


def choose_game():
    while True:
        print("\n1) Number guessing game")
        print("2) Word guessing game (GitHub terms)")
        print("3) Adventure")
        choice = input("Pick a game (1/2/3), or 'q' to quit: ").strip().lower()

        if choice == "1":
            return play_number
        if choice == "2":
            return play_word
        if choice == "3":
            return play_adventure
        if choice.startswith("q"):
            return None
        print("Please enter 1, 2, 3, or q.")


def main():
    print("Welcome! Three games to choose from.")
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
