import os
import random



def read(data_packet='./Files'):

    word = []
    with open(data_packet, 'r', encoding="utf-8") as f:
        for l in f:
            word.append(l.strip().replace(" ","").upper())
    return word

def run():

    choose = int(input("choose an option: 1-test or 2-words: "))

    if choose == 1:
        data = read(data_packet='./Files/test_words.txt')
        
    
    elif choose == 2:
        data = read(data_packet='./Files/words.txt')

    random_word = random.choice(data)

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

if __name__ == '__main__':
    run()