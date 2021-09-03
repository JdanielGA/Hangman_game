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
                                                  |
                                            ============

                                        Do you want to play?
                                        1 - Yes.
                                        2 - No.
"""

exit_menu = """
 Do you want to exit?
 
 1 - Yes.
 2 - No.

"""

games_options = """
 What area do you want to review?

 1 - parts of the house and items inside the home.

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

                    os.system('clear')
                    random_word = read(file='./Files/house_words.txt')
                    print(random_word)
                    input('press enter key')
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