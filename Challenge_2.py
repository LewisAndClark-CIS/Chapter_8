# usr/bin/python3
# Program Name: Challenge_2.py
# Author: Luke Gosnell
# Date: 2/10/2015
# Contributors: Tom Morrissey
print("Turned on the television!")
print("Change channel and adjust volume to your liking!")
print("---------------------------------------------------")

class TV(object):
    def Channel(Channel = 1):
        print ("Current Channel: ", Channel, " First Channel: Last Channel: 100")
        Channel = int(input("Enter Channel: "))
        while Channel > 100 or Channel < 1:
            if Channel > 100:
                print("Please upgrade to get more channels.")
                Channel = int(input("Enter Channel: "))
            elif Channel < 1:
                print("That channel does not exist, silly goose.")
                Channel = int(input("Enter Channel: "))
        return Channel
    def Volume(Volume = 25):
        print ("Current Volume: ", Volume, " Lowest Volume: 0 Highest Volume: 50")
        Volume = int(input("Enter Volume: "))
        while Volume > 50 or Channel < 0:
            if Volume > 50:
                print("WAY TOO LOUD!!")
                Volume = int(input("Enter Volume: "))
            elif Volume < 0:
                print("Volume too low.")
                Volume = int(input("Enter Volume: "))
        return Volume
print("")
print("MENU")
print("____")

choice = 0
Channel=1
Volume=25

print ("Current Channel: ", Channel)
print ("Current Volume: ", Volume)
        
while choice != 1:
    choice = int(input("""
        1 - Turn off television
        2 - Change channel
        3 - Adjust volume

    Choice: """))
    if choice == 2:
        TV.Channel(Channel)
    elif choice == 3:
        TV.Volume(Volume)
    else:
        print("OFF")
        
                        
    
                         

        
    
