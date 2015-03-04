class Television(object):

    def __init__(self, name, channel = 1, volume = 5):
        print("Your new TV came in!")
        self.name = name
        self.channel = channel
        self.volume = volume

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        if newName != "":
            self.__name = newName
            print("Your new TV is now called: ", self.__name)
        else:
            print("Wha-you MUST have a name for your TV! What normal person dosen't name thier TV set?")

            try:
                print("The name remains as: ". self.__name)

            except AttributeError:
                self.__name = "Default"
                print("Your new TV is now called: ", self.__name)

def main():
    tv_name = input("What's your new TV's name? ")
    tv = Television(tv_name)

    choice = None
    while choice != "0":
        print \
        ("""
        TV Maker Menu

        0 - Quit
        1 - TV Explanations
        2 - Set Channel
        3 - Set Volume
        4 - Adjust TV name
        """)

        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Good Bye!")

        elif choice == "1":
            print("Here are the new functions of your TV: ")
            print(tv)

        elif choice == "2":
            amount = int(input("Enter 1 to 100 for a certain channel: "))
            tv.channel = amount

        elif choice == "3":
            amount = int(input("Enter 0 to 10 to set the volume: "))
            tv.volume = amount

        elif choice == "4":
            print("Change the name of your TV set. Make sure you name it something!")
            tv.name = input("Enter your new TV's name here: ")

        else:
            print("\nSorry, but", choice, "isn't a valid choice. Press enter to exit.")
        
    
