#challenge 1
#author: bo meers
#date: friday, may 8th

import random
gameOver = 0
hunger = 100
playtime = 100

while gameOver != 1:
    print("""
    0 - listen to your critters
    1 - feed your critters
    2 - play with your critters
    3 - view critters status
    4 - quit
    """)

    ask = int(input("what would you like to do: "))

    if ask == 0:
        num = random.randint(0,1)
        if num == 0:
            print("They're hungry!")
        elif num == 1:
            print("They want to play!")

    elif ask == 1:
        ask = int(input("How many grams of food: "))
        hunger = hunger - ask
        if hunger > 0:
            print("They're still hungry")
        else:
            print("They're stuffed!")
            

    elif ask == 2:
        ask = int(input("how many minutes will you play with your critters: "))
        playtime = playtime - ask
        if playtime > 0:
            print("That was too short!")
        else:
            print("They cant play anymore!")

    elif ask == 3:
        print("Hunger Level: " + str(hunger))
        print("Energy Level: " + str(playtime))

    elif ask == 4:
        gameOver = 1
