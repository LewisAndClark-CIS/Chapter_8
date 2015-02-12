#! /usr/bin/python3
# Program Name: Thomas Morrissey
# Author: Thomas Morrissey
# Date Written: 2-11-2015

import random
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


def main():
    Boredom = 0
    Hunger = 0
    Farm=[]
    for Number in range(1,5):
        crit_name = input("What do you want to name your critter?: ")
        Boredom = random.randint(1,5)
        Hunger = random.randint(1,5)
        crit=(crit_name, Boredom, Hunger)
        Farm.append(Critter(crit_name, Boredom, Hunger))
    
    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critters
        2 - Feed your critters
        3 - Play with your critters
        """)
    
        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Good-bye.")

        elif choice == "1":
            for crit in Farm:
                crit.talk()
        
        elif choice == "2":
            for crit in Farm:
                crit.eat()
         
        elif choice == "3":
            for crit in Farm:
                crit.play()

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")     
