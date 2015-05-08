#challenge 2
#author: bo meers
#date: friday, may 8th

vol = 25
chan = 10
gameOver = 0

print("You sit down and turn on your tv.")

while gameOver != 1:
    print("\tVolume: " + str(vol))
    print("\tChannel: " + str(chan))
    print("""
0 - adjust volume
1 - change channel
2 - exit
""")
    ask = int(input("What would you like to do: "))
    if ask == 0:
        ask = int(input("How much louder: "))
        vol = vol + ask
    elif ask == 1:
        ask = int(input("What channel: "))
        chan = ask
    elif ask == 2:
        gameOver = 1
