import random
from art import logo


EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


while True:
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess_remains = set_difficulty()
    number_secret = random.randint(1, 100)

    print(f"You have {guess_remains} attempts remaining to guess the number.")

    while guess_remains > 0:
        guess = int(input("Make a guess: "))

        if guess == number_secret:
            print("🎉 Congratulations! You guessed the number! 🏆")
            break
        elif guess < number_secret:
            print("📈 Too low! Try again.")
        else:
            print("📉 Too high! Try again.")

        guess_remains -= 1

        if guess_remains > 0:
            print(f"❤️ You have {guess_remains} attempts remaining.")
        else:
            print(f"💀 You lost! The correct number was {number_secret}.")

    print("🔚 Game over!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
