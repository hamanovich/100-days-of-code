from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5
RANGE = [1, 100]


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    return EASY_LEVEL if difficulty_level == 'easy' else HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {RANGE[0]} and {RANGE[1]}.")
    answer = randint(RANGE[0], RANGE[1])

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
