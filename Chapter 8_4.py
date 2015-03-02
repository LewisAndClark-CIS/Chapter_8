#Chapter 8-4.py
#Karl Pearson
#In collab with Karlos Calvillo and Thomas Morrisey
#3/2/2015

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
    
    def eat(self, food = 0):
        food = int(input("How much food do you want to give " + self.name + "?(lbs) "))
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 0):
        fun = int(input("How much time do you want to play with " + self.name + "?(minutes) "))
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    Boredom=0
    Hunger=0
    Farm=[]
    for Number in range(1,5):
        crit_name=input("What do you want to name your critter? ")
        Boredom=random.randint(1,5)
        Hunger=random.randint(1,5)
        crit=(crit_name,Boredom,Hunger)
        Farm.append(Critter(crit_name,Boredom,Hunger))
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
            for crit in Farm:
                crit.talk()
        
        # feed your critter
        elif choice == "2":
            for crit in Farm:
                crit.eat()
         
        # play with your critter
        elif choice == "3":
            for crit in Farm:
                crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 

