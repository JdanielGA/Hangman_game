import os
import random

words = []

with open('./Files/words.txt', 'r', encoding="utf-8") as f:
    for l in f:
        words.append(l.strip().replace(" ","").upper())

random_word = random.choice(words)

letters_of_test_word = [letter for letter in random_word]
hidden_word = ['_'] * len(random_word)
index_dict = {}

for idx, letter in enumerate(random_word):
        if not index_dict.get(letter): 
            index_dict[letter] = []
        index_dict[letter].append(idx)


print(index_dict)
while True:
    for item in hidden_word:
        print(item, " ", end="")
    print("\n")

    letter = input("Enter a letter: ").strip().upper()
    print(f'The letter chossen was {letter}')

    if letter in letters_of_test_word:
        for idx in index_dict[letter]:
            hidden_word[idx] = letter
    
    if '_' not in hidden_word:
        print('You win')
        break