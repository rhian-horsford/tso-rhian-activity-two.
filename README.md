# Terminal Game Arcade

A compact Python arcade with three different ways to test your luck, memory, and nerve. Launch the menu, pick a mode, and jump straight into a quick terminal game.

## Game Lineup

| Mode | What You Do | Challenge |
| --- | --- | --- |
| **Number Guessing** | Find the computer's secret number between 1 and 100. | Use higher/lower hints and try to solve it in as few guesses as possible. |
| **GitHub Word Guessing** | Reveal a hidden GitHub term one letter at a time. | You get 6 misses. Repeated letters are free, and `!` lets you guess the whole term. |
| **Adventure Run** | Name your hero, choose a class, pick a weapon, and push through five areas. | Manage attacks, defense, potions, and the final boss fight. |

## Quick Start

You only need Python 3.

```bash
python3 main.py
```

When the menu opens, choose one of the three games:

```text
Choose your challenge:
	1) Number Quest      Find the secret number from 1 to 100
	2) GitHub Word Vault Guess the hidden GitHub term
	3) Dungeon Run       Build a hero and face the final boss
```

Type `q` at the menu when you are ready to quit.

## How It Feels

- **Fast to start:** one command, one menu, no setup steps.
- **Replayable:** random numbers, random words, and different adventure encounters keep each run fresh.
- **Beginner-friendly:** each game uses clear prompts and simple terminal input.
- **A little dramatic:** the adventure mode adds classes, weapons, healing choices, and a final prize.

## Project Files

| File | Purpose |
| --- | --- |
| `main.py` | Starts the arcade menu and routes you into the selected game. |
| `number_game.py` | Runs the 1-100 number guessing game. |
| `word_game.py` | Runs the GitHub-term word guessing game. |
| `adventure.py` | Runs the fantasy adventure with character choices and combat. |

## Try a Run

Open a terminal in this folder and run the command above. Pick a game, play a round, then choose whether to return to the main menu or quit.
