import random
from os import system
name = input("Hello what is your name?: ").title()
def clear():
    _ = system('cls')
print(f'Hope you are doing well "{name}".')
yes = 'yes'
while yes == 'yes':
    randomgreet = random.randrange(7)
    input("Ask me something: ")
    if randomgreet == 0:
        print(f'Yes {name}.')
    elif randomgreet == 1:
        print(f"It is certain {name}.")
    elif randomgreet == 2:
        print(f'Without a doubt {name}.')
    elif randomgreet == 3:
        print(f"Concentrate and ask again {name}.")
    elif randomgreet == 4:
        print(f"Very doubtful {name}.")
    elif randomgreet == 5:
        print(f"Cannot predict now. {name} ask me again later.")
    elif randomgreet == 6:
        print(f"Reply hazy try again. {name}")
    else:
        print(f"Probably not {name}.")
    yes = input('Is there another question you want to ask me? Type "yes" or "no".: ')
    clear()
