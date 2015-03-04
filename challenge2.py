#Andrew Hecky
"""
2) Write a program that simulates a television by creating it as an object. The user should
be able to enter a channel number and raise or lower the volume. Make sure that the channel
number and volume level stay within valid ranges.
"""
class tv(object):
    def change_vol(vol):
        change = input("Volume (U)p or (D)own: ")
        while (change.lower() != 'u') and (change.lower() != 'd'): #Validation
            change = input("Enter valid input (U)p or (D)own: ")
        if change.lower() == 'u':
            difference = int(input('Enter how much to increase (0-999): '))
            vol += difference
            if vol > 999: #Checks for valid input
                vol = 999
        else:
            difference = int(input('Enter how much to decrease (0-999): '))
            vol -= difference
            if vol < 0: #Checks for valid input
                vol = 0
        return vol
    def change_chan(chan):
        changeChan = int(input("Enter a channel 1 to 999: "))
        if changeChan < 1: #Checks for valid input
            chan = 1
        elif changeChan > 999:
            chan = 999
        else:
            chan = changeChan
        return chan

chan = 1
vol = 0

print('\tWELCOME TO SKYNETS TELEVISION SERVICE')

choice = -1
while (choice in range(2) or (choice == -1)):
    print("""0 - Change volume : 0 - 999\n
1 - Change channel : 1 - 999\n
2 - Exit\n
    """)
    choice = int(input('Enter choice (0-2): '))
    if choice == 0:
        vol = tv.change_vol(vol)
        print("\nThe volume is now: " + str(vol))
    elif choice == 1:
        chan = tv.change_chan(chan)
        print("\nThe channel is now: " + str(chan))
    else:
        print('Exiting...')
input('Press enter to exit')
