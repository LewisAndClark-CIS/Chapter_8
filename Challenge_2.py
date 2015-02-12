#! usr/bin/python3
# Program Name: Challenge_2.py
# Author: Thomas Morrissey
# Date Written: 2-10-2015

# Pseudocode:
# The Goal of the program is to create a program that acts like a television, where you can change volume settings and channel setteings.
# I will explain how the program works as in comment form.
class Television(object):# This creates the class
    def volume(Volume = 50):# This function changes the volume.
        VolumeChange = 0
        print("Max = 100, Min = 1, Current Volume =", Volume)
        VolumeChange=int(input("How much would you like to change the volume: "))
        Volume = Volume + VolumeChange
        while Volume > 100 or Volume < 1:
            if Volume > 100:
                print("The Volume is too high, setting volume back to 50.")
            elif Volume < 1:
                print("The volume is too low, setting volume back to 50.")
            Volume = 50
            VolumeChange=int(input("How much would you like to change the volume: "))
            Volume = Volume + VolumeChange
        return Volume
    def Channel(Channel = 25):# This sets the Channel
        print("Max = 50, Min = 1, Current Channel =", Channel)
        Channel=int(input("Please enter your channel: "))
        while Channel > 50 or Channel < 1:
            if Channel > 50:
                print("The current volume too high. Resetting the channel back to 25.")
            elif Channel < 1:
                print("The current channel is too low. Resetting the channel back to 25.")
            Channel=int(input("Please enter your channel: "))
        return Channel
    def Status(Volume = 50, Channel = 25):#This function displays the current values
        print("Current Channel:", Channel)
        print("Current Volume:", Volume)
#___________________________Main Functions_______________________________________________
def main():
    Choice = 0# This is sets choice as a int value 
    Volume = 50
    Channel = 25
    print("Welcome to your Television.")
    while Choice != 4:
        print(""" 
Television opitions:
    1 - Change Volume
    2 - Change Channel
    3 - Print Current Status
    4 - Exit""")
        Choice = int(input("Your Choice: "))#This determines what choice the user makes
        if Choice == 1:
            Volume=Television.volume(Volume)
        elif Choice == 2:
            Channel=Television.Channel(Channel)
        elif Choice == 3:
            Television.Status(Volume,Channel)
        elif Choice == 4:
            print("Good bye.")
        else:
            print("That is not a option.")
#_________________________________________________________________________________________
main()            
    
