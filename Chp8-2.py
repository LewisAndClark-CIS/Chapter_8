# Chapter 8 challenge 2
# Author: Alton Stillwell
# Date: 2/11/15
###############
## import / create functions & classes
# import random for random starting volume & channel
import random
# create class to handle the television
class television(object):
# this function will handle the channel
    def change_channel(channel):
        newChannel = int(input("Enter channel ( 1 - 24 ): "))
        if newChannel < 1:
            channel = 1
        elif newChannel > 24:
            channel = 24
        else:
            channel = int(newChannel)
        return channel
# this function will handle the volume
    def change_volume(volume):
        upDown = input("Enter 'up' or 'down' to change volume: ")
        while upDown != "up" and upDown != "down":
            print("Invalid input.")
            upDown = input("Enter 'up' or 'down' to change volume: ")
        amount = int(input("Enter change: "))
        if upDown  == "up":
            volume += amount
            if volume > 50:
                volume = 50
        elif upDown == "down":
            volume -= amount
            if volume < 0:
                volume = 0
        else:
                print("Something has gone horribly wrong :O")
        return volume
# this function is the main program loop and initilizer
def main():
    channel = random.randint(1, 24)
    volume = random.randint(0, 50)
    print()
    print("Current Channel: ", channel)
    print("Current Volume: ", volume)
    print("""
    1 - Change Channel ( 1 - 24 )
    2 - Change Volume ( 0 - 50 )
    3 - Power Off
    """)
    choice = input("Enter choice: ")
    while choice != "3":
        if choice == "1":
            channel = television.change_channel(channel)
        elif choice == "2":
            volume = television.change_volume(volume)
        else:
            print("Invalid choice.")
        print()
        print("~~~~~~~~~~~~~~~~~~")
        print()
        print("Current Channel: ", channel)
        print("Current Volume: ", volume)
        print("""
    1 - Change Channel ( 1 - 24 )
    2 - Change Volume ( 0 - 50 )
    3 - Power Off
    """)
        choice = input("Enter choice: ")
##########################
# call main
main()
# ending text
print()
print("Powering down...")
input("\n\nPress <enter> to exit")
