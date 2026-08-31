"""Entry point: pick one of the three games."""

from adventure import play_adventure
from number_game import play_number
from word_game import play_word


def choose_game():
    while True:
        print("\nChoose your challenge:")
        print("  1) Number Quest      Find the secret number from 1 to 100")
        print("  2) GitHub Word Vault Guess the hidden GitHub term")
        print("  3) Dungeon Run       Build a hero and face the final boss")
        choice = input("\nEnter 1, 2, 3, or q to quit: ").strip().lower()

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
    print("=" * 52)
    print("          TERMINAL GAME ARCADE")
    print("=" * 52)
    print("Three quick games. One tiny command-line arcade.")
    try:
        while True:
            game = choose_game()
            if game is None:
                break
            game()
            while True:
                next_step = input("\nReturn to the main menu or quit? (m/q): ").strip().lower()
                if next_step == "m":
                    break
                if next_step == "q":
                    print("Thanks for playing!")
                    return
                print("Please enter m for menu or q to quit.")
        print("Thanks for playing!")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
