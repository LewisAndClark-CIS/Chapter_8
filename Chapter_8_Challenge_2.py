# TV.py
# Created by: Zach Golik y Brianna Melius
# Date: 02/08/15

class Television(object):
    """A tv"""
    def __init__(self, number = 0, volume = 0):
        self.number = number
        self.volume = volume

    def volume_change(self):
        askVolume = input("Would you like to turn the volume up or down(u/d)? ")
        while askVolume != 'u' and askVolume != 'd':
            askVolume = input("Please enter up or down(u/d): ")
        if askVolume == "u":
            self.volume += 1
            if self.volume >10:
                self.volume = 10
        else:
            self.volume -= 1
            if self.volume < 0:
                self.volume = 0
        print("The volume is at", self.volume, "now.")

    def channel(self):
        askChannel = input("Would you like to turn the channel up or down(u/d)? ")
        while askChannel != 'u' and askChannel != 'd':
            askChannel = input("Please enter up or down(u/d): ")
        if askChannel == 'u':
            self.number += 1
            if self.number > 10:
                self.number = 10
        else:
            self.number -= 1
            if self.number < 0:
                self.number = 0
        print("The channel is at", self.number, "now.")

    def current(self):
        print("You are on channel", str(self.number)+ ".")
        print("The volume is at", str(self.volume)+ ".")

def main():
    tv = Television()

    volume = 0
    number = 0
    choice = None
    while choice != "0":
        print \
        ("""
        Digital Television

        0 - Quit
        1 - Current televison status
        2 - Turn up the volume
        3 - Change the channel
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == '0':
            print("Good-bye.")

        # tv status
        elif choice == '1':
            tv.current()
            
        # volume status
        elif choice == '2':
            tv.volume_change()

        # channel status
        elif choice == '3':
            tv.channel()

        # unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
