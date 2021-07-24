import os
import random

def star_menu():
    flag_a = True

    while flag_a:
        os.system("clear")
        opcion = int(input("""
 Do you want to exit?

    1 for Yes
    2 for No

 Please, select a number:"""))
        if opcion == 1:
            flag_a = False    
        else:
            flag_a = True
            
    
    print("\n","thanks")


def read():
    words = []
    with open("./Files/words.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    random_word = random.choice(words)
    print(random_word)


def run():
    read()
      

if __name__=='__main__':
    run()