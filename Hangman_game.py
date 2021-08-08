import os
import random

# flag = True

my_test_word = 'celphone'.upper()
letters_of_test_word = [letter for letter in my_test_word]
hidden_word = ['_'] * len(my_test_word)
index_dict = {}

for idx, letter in enumerate(my_test_word):
        if not index_dict.get(letter): 
            index_dict[letter] = []
        index_dict[letter].append(idx)

# chosen_word = input('chose one letter: ')

# find_letter = my_test_word.find(chosen_word)

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


# def main_menu():
#     print(f"""
# Welcome.

# the word is {my_test_word}
# """)


# while flag:
#     os.system('clear')
#     main_menu()
#     chosen_letter = str(input('choice one letter or number 1 to exit: ')).upper()
#     var = len(chosen_letter)

#     if var >= 0:
#         if chosen_letter == '1':
#             os.system('clear')
#             print('')
#             print('Thanks')
#             print('')
#             flag = False
        
#         else:
#             os.system('clear')
#             print('')
#             print(f'The chosen letter was {chosen_letter}')
#             print('')
#             choice = input('type Enter key')
#     else:
#         os.system('clear')
#         print('empy')
#         print('')
#         choice = input('type Enter key')
    