Choice = 0
channel=0
volume=0
while Choice != 4:
    print('''
Welcome Human!
-------------------------
1 - Change Channel
2 - Change Volume
3 - Status
4 - Exit
-------------------------
''')
    Choice = int(input('Choose: '))
    if Choice == 1:
        channel = int(input('What channel? '))

    elif Choice == 2:
        volume = int(input('Volume Level: '))

    elif Choice == 3:
        print('You are on Channel ' + str(channel) + '.')
        print('Volume Level:', str(volume))

    elif Choice == 4:
        print('See you later')

    else:
        print('INVALID OPTION!')

        
