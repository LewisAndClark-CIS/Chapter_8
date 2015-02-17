# usr/bin/python3
# Program Name: Challenge_1.py
# Author: Luke Gosnell
# Date: 2/11/2015
# Contributors: Thomas Morrissey
# Critter Caretaker
# A virtual pet to care for

critterCount = 0
ctitterList = []
while critterCount < 10:
    class Critter(object):
        """A virtual pet"""
        critterCount = critterCount + 1
        def __init__(self, name, hunger = 0, boredom = 0):
            self.name = name
            self.hunger = hunger
            self.boredom = boredom

        def __pass_time(self):
            self.hunger += 1
            self.boredom += 1

        @property
        def mood(self):
            unhappiness = self.hunger + self.boredom
            if unhappiness < 5:
                m = "happy"
            elif 5 <= unhappiness <= 10:
                m = "okay"
            elif 11 <= unhappiness <= 15:
                m = "frustrated"
            else:
                m = "mad"
            return m
        
        def talk(self):
            print("I'm", self.name, "and I feel", self.mood, "now.\n")
            self.__pass_time()
        
        def eat(self, food = 4):
            food = int(input("How much food? "))
            print("Brruppp.  Thank you.")
            self.hunger -= food
            if self.hunger < 0:
                self.hunger = 0
            self.__pass_time()

        def play(self, fun = 4):
            fun = int(input("How many hours of fun? "))
            print("Wheee!")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom = 0
            self.__pass_time()
        def __str__(self):
            print("Name: ", self.name)
            print("Boredom: ", self.boredom)
            print("Hunger: ", self.hunger)
            return "Returning to main menu"
        
        
def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            crit.eat()
         
        # play with your critter
        elif choice == "3":
            crit.play()

        elif choice == "4":
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")
    critterList.append(Critter)

main()
("\n\nPress the enter key to exit.") 

