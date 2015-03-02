#Chapter_8_2
#Karlos Calvillo

class Television(object):

    def Channel(Channel):
        print("min = 1, max = 100, current ->",Channel)
        Channel = int(input("What channel do you want to watch? "))
        while 1 > Channel > 100:
            if Channel > 100:
                print("Your Channel is too high, please re-enter your Channel.")
            elif Channel < 1:
                print("Your channel is too low, please re-enter your Channel.")
                Channel = int(input("What channel do you want to watch? "))
        return Channel
    def Volume(Volume):
        print("Max -> 50, Min -> 1, Current ->", Volume)
        Volume = int(input("What volume would you like to set the TV at? "))
        while 1 > Volume > 50:
            if Volume > 50:
                print("Volume is too high, please re-enter your volume.")
            elif Volume < 1:
                print("Volume is too low, please re-enter your Volume.")
            Volume = int(input("What volume would you like to set the TV at? "))
        return Volume

def main():
    Channel=50
    Volume=25
    choice = None  
    while choice != "0":
        print \
        ("""
        TV Maker
    
        0 - Quit
        1 - Set Channel
        2 - Set Volume
        """)
    
        choice = input("Choice: ")
        print()
        
        if choice == "0":
            print("Good-bye.")
        
        elif choice == "1":
            Channel=Television.Channel(Channel)
         
        
        elif choice == "2":
            Volume=Television.Volume(Volume)

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
