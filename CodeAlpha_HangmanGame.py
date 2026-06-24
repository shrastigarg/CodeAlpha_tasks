import random
import os


# HANGMAN DELUXE


HANGMAN_PICS = [
"""
  +---+
      |
      |
      |
     ===
""",
"""
  +---+
  O   |
      |
      |
     ===
""",
"""
  +---+
  O   |
  |   |
      |
     ===
""",
"""
  +---+
  O   |
 /|   |
      |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
      |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
 /    |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
 / \\  |
     ===
"""
]

WORDS = {
    "easy": ["cat", "dog", "book", "fish", "tree", "guess"],
    "medium": ["python", "laptop", "garden", "planet", "magnet"],
    "hard": ["algorithm", "developer", "artificial", "database", "activity"]
}


def get_highscore():
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        return int(f.read())


def save_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


def choose_word():
    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter choice: ")

    if choice == "1":
        return random.choice(WORDS["easy"])
    elif choice == "2":
        return random.choice(WORDS["medium"])
    else:
        return random.choice(WORDS["hard"])


def play_game():
    word = choose_word()
    guessed = []
    wrong = 0
    max_wrong = 6

    print("\n🎮 Game Started!")

    while wrong < max_wrong:

        print(HANGMAN_PICS[wrong])

        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        if "_" not in display:
            print("\n🎉 You Won!")
            return True

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter ONE letter only!")
            continue

        if guess in guessed:
            print("Already guessed!")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print("❌ Wrong Guess!")

    print(HANGMAN_PICS[6])
    print("\n💀 Game Over!")
    print("Correct word was:", word)

    return False


def main():

    print("-" * 40)
    print("      🎯 HANGMAN DELUXE")
    print("-" * 40)

    player = input("Enter your name: ")

    score = 0
    highscore = get_highscore()

    print(f"\nWelcome {player}")
    print("Current High Score:", highscore)

    while True:

        win = play_game()

        if win:
            score += 10

        print("\nYour Score:", score)

        if score > highscore:
            highscore = score
            save_highscore(highscore)
            print("🏆 NEW HIGH SCORE!")

        again = input("\nPlay Again? (y/n): ").lower()

        if again != "y":
            break

    print("\nThanks for playing!")
    print("Final Score:", score)
    print("High Score:", highscore)


main()