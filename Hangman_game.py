import os
import random


menu = """

                                    _                              _         
                    __ __ __  ___  | |  __   ___   _ __    ___    | |_   ___ 
                    \ V  V / / -_) | | / _| / _ \ | '  \  / -_)   |  _| / _ \ 
                     \_/\_/  \___| |_| \__| \___/ |_|_|_| \___|    \__| \___/
                    
  _   _                                                          ____                            
 | | | |   __ _   _ __     __ _   _ __ ___     __ _   _ __      / ___|   __ _   _ __ ___     ___ 
 | |_| |  / _` | | '_ \   / _` | | '_ ` _ \   / _` | | '_ \    | |  _   / _` | | '_ ` _ \   / _ \ 
 |  _  | | (_| | | | | | | (_| | | | | | | | | (_| | | | | |   | |_| | | (_| | | | | | | | |  __/
 |_| |_|  \__,_| |_| |_|  \__, | |_| |_| |_|  \__,_| |_| |_|    \____|  \__,_| |_| |_| |_|  \___|
                          |___/  


                                              +---+
                                              |   |
                                              ¨   |
                                                  |
                                                  |
                                            ¯¯¯¯¯ |
                                            ============

                                        Do you want to play?
                                        1 - Yes.
                                        2 - No.
"""

hangman_pick = ["""
                                              +---+
                                              |   |
                                              ¨   |
                                                  |
                                                  |
                                            ¯¯¯¯¯¯|
                                            ============
""", """
                                              +---+
                                              |   |
                                              O   |
                                                  |
                                                  |
                                            ¯¯¯¯¯¯|
                                            ============
""", """
                                              +---+
                                              |   |
                                              O   |
                                              |   |
                                                  |
                                            ¯¯¯¯¯¯|
                                            ============
""", """
                                              +---+
                                              |   |
                                             \O   |
                                              |   |
                                                  |
                                            ¯¯¯¯¯¯|
                                            ============
""", """
                                              +---+
                                              |   |
                                             \O/  |
                                              |   |
                                                  |
                                            ¯¯¯¯¯¯|
                                            ============
""", """
                                              +---+
                                              |   |
                                             \O/  |
                                              |   |
                                             /    |
                                            ¯¯¯¯¯¯|
                                            ============
""", """
                                              +---+
                                              |   |
                                             \O/  |
                                              |   |
                                             / \  |
                                            ¯¯¯¯¯¯|
                                            ============
""", """
                                              +---+
                                              |   |
                                              |   |
                                              0   |
                                             /|\  |
                                             / \  |
                                            ============
"""]

exit_menu = """
 Do you want to exit?
 
 1 - Yes.
 2 - No.

"""

games_options = """
 What area do you want to review?

 1 - parts of the house and items inside the home.

"""
play_again = """
 Do you want to play again?

 1 - Yes
 2 - No

 choose an opcion: 
"""

def read(file):
    words = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            words.append(str(line))
    
    random_word = random.choice(words)
    
    return random_word


def run():

    flag = True

    while flag:

        os.system('clear')
        print(menu)
        election = int(input("choose an option: "))

        if election == 1:

            flag_2 = True

            while flag_2:

                os.system('clear')
                print(games_options)
                game_choice = int(input('chosse an option: '))

                if game_choice == 1:

                    flag_3 = True

                    while flag_3 ==True:

                        random_word = read(file='./Files/house_words.txt')

                        lives = 7
                        position = 0
                        end_game = True

                        while True:

                            if lives > 0:
                                os.system('clear')
                                print(hangman_pick[position])
                                print(random_word)
                                e = input('choose an option Y or N to continue: ')

                                if e == 'Y':
                                    continue

                                elif e == 'N':
                                        lives -= 1
                                        position += 1

                            elif lives == 0:
                                os.system('clear')
                                print(hangman_pick[position])
                                print('You lose \n')
                                end_game = False
                                break

                        if end_game == False:
                            try_again = int(input(play_again))
                            if try_again == 1:
                                end_game = True
                            else:
                                break                            
                        
                else:
                    flag_2 = False

        else:
            os.system('clear')
            print(exit_menu)
            exit_choice = int(input('choose an option: '))

            if exit_choice == 2:
                flag = True
            else:
                os.system('clear')
                print('Thanks for playing \n')
                flag = False
      

if __name__=='__main__':
    run()
