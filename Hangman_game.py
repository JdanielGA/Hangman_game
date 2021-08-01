import os
import random

def choosing_word():
    words = []
    with open("./Files/words.txt", "r") as f:
        for line in f:
            words.append(line.strip().upper())
    
    chosen_word = random.choice(words)
    print(chosen_word)
