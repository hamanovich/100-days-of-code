import random
from hangman_stages import stages
from hangman_words import word_list
from hangman_logo import logo

DISPLAY_CHAR = "_"
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = len(stages) - 1

print(logo)
print(f'\nThe solution is `{chosen_word}`.\n')

# Create blanks
display = [DISPLAY_CHAR] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if DISPLAY_CHAR not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
