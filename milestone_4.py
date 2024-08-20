import random

word_list = ["apple", "pineapple", "orange", "mango", "pomegranate", "strawberry"]

class Hangman:
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = 0
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess: str):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess, {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter in the word: ")
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

hangman = Hangman(word_list=word_list)
hangman.ask_for_input()
