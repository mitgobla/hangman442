import random

word_list = ["apple", "pineapple", "orange", "mango", "pomegranate", "strawberry"]

class Hangman:
    def __init__(self, word_list: list, num_lives: int = 5):
        self.__word_list = word_list
        self.__word = random.choice(self.__word_list)
        self.__word_guessed = ['_'] * len(self.__word)
        self.num_letters = len(set(self.__word))
        self.num_lives = num_lives
        self.__list_of_guesses = []

    def _check_guess(self, guess: str):
        """Check if a letter is in the randomly picked word.

        Args:
            guess (str): The character to check is present.
        """
        guess = guess.lower()
        if guess in self.__word:
            print(f"Good guess, {guess} is in the word.")
            for index, letter in enumerate(self.__word):
                if guess == letter:
                    self.__word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        """Ask for a letter input from the user."""
        while True:
            print(' '.join(self.__word_guessed))
            guess = input("Guess a letter in the word: ")
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.__list_of_guesses:
                print("You've already tried that letter!")
            else:
                self._check_guess(guess)
                self.__list_of_guesses.append(guess)
                break

def play_game(word_list: list):
    """Play a game of Hangman.

    Args:
        word_list (list): The list of words that you can guess from.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break

        if game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

        game.ask_for_input()

play_game(word_list)
