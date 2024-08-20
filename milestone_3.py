import random

word_list = ["apple", "pineapple", "orange", "mango", "pomegranate", "strawberry"]
word = random.choice(word_list)

def ask_for_input() -> None:
    while True:
        guess = input("Take a guess with a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess: str) -> None:
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()