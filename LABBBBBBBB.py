print("""
welcome to the tv progrqam!!
    """)
Choice = 0
aux=50
channel=4
while Choice != 4:
    Choice=int(input("""what channel would you like to view
1 - Aux
2 - News
3 - Cartoons
4 - off
"""))
    if Choice == 1:
        print("*loud screching sounds*")
        aux=int(input('What volume would you like (0-100)'))
        while aux >100 or aux<0:
            aux=int(input('|||||||||||||---'))
    elif Choice == 2:
        print("And welcome to the new in todays date a man was killed by a evil bannana")
        
    elif Choice==3:
        print("Hey willy watch out for that safe")
    elif Choice == 4:
        print("Good Bye!")
    else:
        print("INVALID OPTION!!")
    
    
