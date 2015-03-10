class TV(object):
    def volume(volume=50):
        
        print("Max = 100, Min: = 0, Current Volume = "+str(volume))
        volume=int(input("What would you like the volume to be? "))
        
        while volume > 100 or volume < 0:
            if volume > 100:
                print("Too high. Setting volume to 50.")
            elif volume < 1:
                print("Too low. Setting volume to 50.")
            volume = 50
        print("Volume is "+str(volume))
        return volume

    def channel(channel=25):
        print("Max = 50, Min = Aux, Current Channel = "+str(channel))
        channel = input("Enter your channel: ")
        try:
            channel=channel.upper()
            if channel=="AUX":
                print("Channel is AUX.")
        except AttributeError:
            print("")
            
        try:
            while int(channel) > 50 or int(channel) <1:
                if int(channel) > 50:
                    print("Out of range. Resetting to 25.")
                    channel=25
                elif int(channel) < 1:
                    print("Out of range. Resetting to 25.")
                    channel = 25
            print("Channel is "+str(channel)+".")
        except ValueError:
            if channel!="AUX":
                print(channel+" is not a valid option, resetting to 25.")
                channel=25
        
        return channel

    def status(volume, channel):
        print("Current channel: "+str(channel))
        print("Current volume: "+str(volume))



def main(volume, channel):
    choice=0
    print("Welcome to your T.V.")
    while choice !=4:
        print("""
T.V. options:
    1-Change Volume
    2-Change Channel
    3-Print Current Status
    4-Exit""")
        choice = int(input("Your Choice: "))
        if choice == 1:
            volume=TV.volume(volume)
        elif choice==2:
            channel=TV.channel(channel)
        elif choice == 3:
            TV.status(volume,channel)
        elif choice ==4:
            input("Press <enter> to exit...")
        else:
            print("That is not an option.")

main(volume=50, channel=25)

            
