import random

word_list = ["Apple", "Pineapple", "Orange", "Mango", "Pomegranate", "Strawberry"]
word = random.choice(word_list)

while True:
    guess = input("Take a guess with a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")