# Virtual Television

class TV(object):
    """A virtual TV"""

    # TV Channel
    def channel(self):
        print("""
              Choose Your channel
              1 - ESPN
              2 - Fox
              3 - CW
              4 - Syfy
              """)
        channell = input("What channel do you want to watch? ")
        if channell == "1":
            print("Your watching ESPN")
        elif channell == "2":
            print("Your watching Fox")
        elif channell == "3":
            print("Your watching CW")
        elif channell == "4":
            print("Your watching Syfy")
        else:
            print("Sorry invalid channel...choose again")
            channell = input("What channel do you want to watch? ")

    # Volume Level       
    def volume(self):
        print(" 1-2-3-4-5-6-7-8-9-10 ")
        lvl = int(input("What would you like the volume to be? "))
        if 10 >= lvl >= 1:
            print("Your volume level is currently at", lvl)
        else:
            print("That is not a valid volume level.")
            lvl = int(input("What would you like the volume to be? "))
            print("Your volume level is currently at", lvl)
        


def main():
    tv = TV()
    decision = None
    while decision == "channel" or "volume":
        decision = input("Do you want to pick a channel or change the volume? ")
        if decision == "channel":
            tv.channel()
        elif decision == "volume":
            tv.volume()

main()
("\n\nPress the enter key to exit.")

