

import random

# ── Hangman ASCII art stages (0 = full hang, 6 = empty gallows) ──
HANGMAN_STAGES = [
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
  """,
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
  """,
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========
  """,
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========
  """,
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========
  """,
    """
   -----
   |   |
   O   |
       |
       |
       |
=========
  """,
    """
   -----
   |   |
       |
       |
       |
       |
=========
  """,
]

WORDS = ["python", "hangman", "keyboard", "science", "jungle"]
MAX_WRONG = 6


def display_state(wrong_guesses: int, guessed: set, word: str) -> None:
    """Print the gallows, the word progress, and wrong letters."""
    print(HANGMAN_STAGES[MAX_WRONG - wrong_guesses])
    # Word display  e.g.  p _ t h o n
    display_word = " ".join(ch if ch in guessed else "_" for ch in word)
    print(f"  Word : {display_word}")
    wrong_letters = sorted(ch for ch in guessed if ch not in word)
    print(f"  Wrong letters ({wrong_guesses}/{MAX_WRONG}): {', '.join(wrong_letters) or '—'}\n")


def get_valid_input(guessed: set) -> str:
    """Ask until the player enters a single unseen letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.")
        elif guess in guessed:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play() -> None:
    word = random.choice(WORDS)
    guessed: set = set()
    wrong_guesses = 0

    print("\n" + "=" * 40)
    print("       Welcome to Hangman! 🎯")
    print("=" * 40)
    print(f"  The word has {len(word)} letters. You have {MAX_WRONG} attempts.\n")

    while True:
        display_state(wrong_guesses, guessed, word)

        # Win check
        if all(ch in guessed for ch in word):
            print(f"  🎉 You won! The word was '{word.upper()}'.")
            break

        # Lose check
        if wrong_guesses >= MAX_WRONG:
            print(f"  💀 Game over! The word was '{word.upper()}'.")
            break

        letter = get_valid_input(guessed)
        guessed.add(letter)

        if letter in word:
            print(f"  ✅ '{letter}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"  ❌ '{letter}' is NOT in the word.")


def main() -> None:
    while True:
        play()
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("  Thanks for playing! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()
