# need to take the users name
# then have some selection of a word from a list of words
# select the number of tries
# implement guessing logic
# if the letter guessed is in the word, then print it in the correct places
# if not, then add a limb to the hang man

#           _________
#           |       |
#           O       |
#         --|--     |
#          / \      |
#                   |
#                ___|___

import random


# need to take the users name
def get_name():
    name = str(input("What is your name? "))
    print("Hello " + name)

# then have some selection of a word from a list of words
def choose_word():
    words_list = [
        "act", "apple", "bird", "boat", "book", "boy", "cat", "clock", "cloud",
        "cold", "dark", "door", "fire", "fish", "flag", "foot", "game", "hand",
        "lake", "leaf", "life", "milk", "moon", "name", "neck", "nest", "post",
        "pull", "rock", "snow"
    ]

    # select the word randomly
    current_word = random.choice(words_list)
    return current_word

# show the word, with correct guessed
def display_word(word,guessed_letters):
    displayed = ''

    #check guessed letters
    for letter in word:
        if letter in guessed_letters:
            #show letter if guessed
            displayed += letter
        else:
            #show blank if not guessed
            displayed += '_'

    print(displayed)

def display_man(wrong_guesses):
    if wrong_guesses == 0:
        print("""
                _________
                |       |
                        |
                        |
                        |
                        |
                     ___|___
           """)
    elif wrong_guesses == 1:
        print("""
                _________
                |       |
                O       |
                        |
                        |
                        |
                     ___|___
           """)
    elif wrong_guesses == 2:
        print("""
                _________
                |       |
                O       |
                |       |
                        |
                        |
                     ___|___
           """)
    elif wrong_guesses == 3:
        print("""
                _________
                |       |
                O       |
              --|       |
                        |
                        |
                     ___|___
           """)
    elif wrong_guesses == 4:
        print("""
                _________
                |       |
                O       |
              --|--     |
                        |
                        |
                     ___|___
           """)
    elif wrong_guesses == 5:
        print("""
                _________
                |       |
                O       |
              --|--     |
               /        |
                        |
                     ___|___
           """)
    else:
        print("""
                _________
                |       |
                O       |
              --|--     |
               / \      |
                        |
                     ___|___
           """)


def hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    tries = 6

    print("Welcome to Hangman!")
    get_name()
    print("Guess the word!")

    while tries > 0:
        display_man(wrong_guesses)
        display_word(word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            tries -= 1
            print(f"Wrong guess! You have {tries} attempts left.")
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if tries == 0:
        display_man(wrong_guesses)
        print("Sorry, you lost! The word was:", word)

if __name__ == "__main__":
    hangman()