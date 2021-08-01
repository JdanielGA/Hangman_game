import os
import random

def choosing_word():
    words = []
    with open("./Files/words.txt", "r") as f:
        for line in f:
            words.append(line.strip().upper())

    chosen_word = random.choice(words)
    censored_word = '_ ' * len(chosen_word)

    return chosen_word, censored_word


chosen_word, censoring_word = choosing_word()

print(chosen_word)
print(censoring_word)