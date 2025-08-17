import random

def scramble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def word_scramble_game():
    words = ["python", "program", "scramble", "computer", "science", "keyboard"]
    original_word = random.choice(words)
    scrambled = scramble_word(original_word)

    print("Welcome to the Word Scramble Game!")
    print("Scrambled word:", scrambled)

    guess = input("Your guess: ")

    if guess.lower() == original_word:
        print("Correct! ")
    else:
        print(f"Oops! The correct word was: {original_word}")

# Run the game
word_scramble_game()
