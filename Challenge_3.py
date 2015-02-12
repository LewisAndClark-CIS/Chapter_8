#! /usr/bin/python3
# Program Name: Challenge_3.py
# Author: Thomas Morrissey
# Date Written: 2-11-2015

# Pseudocode:
# The Goal of this Challenge is to print the status of our little Critter using the '__str__' command for our class system.
# Please follow the commits as I explain what I did.
class Critter(object):
    """A virtual pet"""
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
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def __str__(self):# This is the command it self, it prints the critter's name, boredom Lv, Hunger Lv, and a message that takes the user back to the Main Menu of the program.
        print("Critter's name:", self.name)
        print("Boredom Level:", self.boredom)
        print("Hunger Level:",self.hunger)
        return "Returning to Main Menu"

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != 0:
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = int(input("Choice: "))
        print()

        if choice == 0:
            print("Good-bye.")

        elif choice == 1:
            crit.talk()
        
        elif choice == 2:
            crit.eat()
         
        elif choice == 3:
            crit.play()

        elif choice == 4:# This activates the str command.
            print(crit)

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
