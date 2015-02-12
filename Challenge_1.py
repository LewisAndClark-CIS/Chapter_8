#! usr/bin/python3
# Program Name: Challenge_1.py
# Author: Thomas Morrissey
# Date written: 2-10-2015

# Pseudocode:
# The goal of this challegne is to change the two options, food from the "def eat" function,
# and fun from "def play", and change these two options into user input assigned varables.

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
    
    def eat(self, food = 0):# I first set food to 0.
        food = int(input("How many ounces do you want me to eat? "))# Then I let the user assign food a value.
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 0):# I next set fun to 0.
        fun = int(input("How many hours do you want to play with me? "))#Then I let the user assign fun a value.
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


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

        if choice == "0":
            print("Good-bye.")

        elif choice == "1":
            crit.talk()
        
        elif choice == "2":
            crit.eat()
         
        elif choice == "3":
            crit.play()

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
