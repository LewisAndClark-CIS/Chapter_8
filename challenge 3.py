#challenge 1
#author: bo meers
#date: friday, may 8th

import random
gameOver = 0
hunger = 100
playtime = 100

while gameOver != 1:
    print("""
    0 - listen to your critter
    1 - feed your critter
    2 - play with your critter
    3 - view critter status
    4 - quit
    """)

    ask = int(input("what would you like to do: "))

    if ask == 0:
        num = random.randint(0,1)
        if num == 0:
            print("I'm hungry!")
        elif num == 1:
            print("i want to play!")

    elif ask == 1:
        ask = int(input("How many grams of food: "))
        hunger = hunger - ask
        if hunger > 0:
            print("Im still hungry")
        else:
            print("Sorry i'm stuffed!")
            

    elif ask == 2:
        ask = int(input("how many minutes will you play with your critter: "))
        playtime = playtime - ask
        if playtime > 0:
            print("That was too short!")
        else:
            print("i cant play anymore!")

    elif ask == 3:
        print("Hunger Level: " + str(hunger))
        print("Energy Level: " + str(playtime))

    elif ask == 4:
        gameOver = 1
