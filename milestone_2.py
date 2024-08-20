import random

word_list = ["Apple", "Pineapple", "Orange", "Mango", "Pomegranate", "Strawberry"]
word = random.choice(word_list)
print(word)

guess = input("Take a guess: ")
if len(guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyz':
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")