#Colaboration on Chapter 8 with Sam Coon and Tyler Kapusniak
#2/10/15

class TV(object):
    def __init__(self, channel = 0, volume = 0):
        self.__channel = channel
        self.__volume = volume
        
    def choose_channel(self):
        print(
            """
    Channels:
    1. Action
    2. Comedy
    3. Romance
    4. History
            """)
        self.__channel = int(input("Choose the channel you want to watch: "))
            
        if self.__channel == 1:
            print("\nYou are on channel 1, the Action channel.")
            print("Your volume is on " + str(self.__volume) + ".\n")
            
        elif self.__channel == 2:
            print("\nYou are on channel 2, the Comedy channel.")
            print("Your volume is on " + str(self.__volume) + ".\n")
            
        elif self.__channel == 3:
            print("\nYou are on channel 3, the Romance channel.")
            print("Your volume is on " + str(self.__volume) + ".\n")
            
        elif self.__channel == 4:
            print("\nYou are on channel 4, the History channel.")
            print("Your volume is on " + str(self.__volume) + ".\n")
            
        else:
            print("That is not an available please choose a different channel.")
                       
    def choose_volume(self):
        self.__volume = int(input("What do you want to set the volume to?(max 100) "))
        
        if self.__volume <= 100 and self.__volume >= 0:
            if self.__volume < 50:
                print("Your volume is at "+ str(self.__volume) + ".")
                
            elif self.__volume >= 50 and self.__volume <= 100:
                print("Your volume is a little loud!")
                
            elif self.__volume <= 0 and self.__volume >= 100:
                print("Can't do that.")
            
        print("You're on channel " + str(self.__channel) + ".")
def main():
    
    chan = TV()
    menu = 19
    while menu != 0:
        
        print(
            """
        0. Turn off TV
        1. Change channel
        2. Change volume
        """)

        menu = int(input("Enter the number of what you want to do: "))

        if menu == 0:
            print("The TV is off.")

        elif menu == 1:
            chan.choose_channel()

        elif menu == 2:
            chan.choose_volume()
            
        elif menu == "":
            print("That is not a valid option please try again")
            
            
        else:
            print("That is not a valid option please try again.")
            

main()

