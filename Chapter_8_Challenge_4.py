# Challange 4
# By: Zachary Michael Joseph Anthony Golik y Brianna Nicole Melius
# Date: 10/02/15

import random

class Critter_One(object):
    """A virtual pet"""
    def __init__(self, name, hunger = random.randint(0, 10), boredom = random.randint(0, 10)):
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
    
    def eat(self, food):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

class Critter_Two(object):
    """A virtual pet"""
    def __init__(self, name, hunger = random.randint(0, 10), boredom = random.randint(0, 10)):
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
    
    def eat(self, food):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

class Critter_Three(object):
    """A virtual pet"""
    def __init__(self, name, hunger = random.randint(0, 10), boredom = random.randint(0, 10)):
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
    
    def eat(self, food):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name1 = input("What do you want to name critter one?: ")
    crit1 = Critter_One(crit_name1)
    crit_name2 = input("What do you want to name critter two?: ")
    crit2 = Critter_Two(crit_name2)
    crit_name3 = input("What do you want to name critter three?: ")
    crit3 = Critter_Three(crit_name3)

    choice = None
    while choice != "0":
        print \
        ("""
         Critter Farm

         0 - Quit
         1 - Listen to your critters
         2 - Feed your critters
         3 - Play with your critters
         """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit1.talk()
            crit2.talk()
            crit3.talk()

        # feed your critter
        elif choice == "2":
            food = int(input("How much food do you want to feed your critter? "))
            while food not in range(1, 11):
                print("A number between 1 and 10!!!")
                food = int(input("How much food do you want to feed your critter? "))
            crit1.eat(food)
            crit2.eat(food)
            crit3.eat(food)

        # play with your critter
        elif choice == "3":
            fun = int(input("How long would you like to play with your pet? "))
            while fun not in range(1, 11):
                print("A number between 1 and 10!!!")
                fun = int(input("How long would you like to play with your pet? "))
            crit1.play(fun)
            crit2.play(fun)
            crit3.play(fun)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
