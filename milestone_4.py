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