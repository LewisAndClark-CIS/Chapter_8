class TV(object):
    def volume(volume=50):
        volumeChange=0
        print("Max = 100, Min: = 0, Current Volume ="+volume)
        volumeChange=int(input("How much would you like to change the volume? "))
        volume+=volumeChange
        while volume > 100 or volume < 0:
            if volume > 100:
                print("Too high. Setting volume to 50.")
            elif volume < 1:
                print("Too low. Setting volume to 50.")
            volume = 50

            volumeChange = int(input("How much would you like to change the volume? "))
            volume+=volumeChange
        return volume

    def channel(channel=25):
        print("Max = 50, Min = Aux, Current Channel ="+channel)
        while channel > 50 or channel <1:
            if channel > 50:
                print("Out of range. Resetting to 25.")
            elif channel < 1:
                print("Out of range. Resetting to 25.")

            channel = 25
            
