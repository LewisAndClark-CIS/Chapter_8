class Television(object):

    def __init__(self, volume, channel):
        self.volume = volume
        self.channel = channel

    def volumeUp(self):
        volume = self.volume
        volume += 1
        return volume

    def volumeDown(self):
        volume = self.volume
        volume -= 1
        return volume

    def changeChannel(self):
        channel = int(input("Channel: "))
        return channel


def main():
    choice = None

    while choice != "0":

        print('''
            1 - Change channel
            2 - Volume Up
            3 - Volume Down
            0 - Power Off
            ''')
        choice = input("Choice: ")

        if choice == "1":
            Television.changeChannel(1)

        elif choice == "2":
            Television.volumeUp(1)

        elif choice == "3":
            Television.volumeDown(1)

        elif choice.upper() == "0":
            print("Good-Bye")

main()