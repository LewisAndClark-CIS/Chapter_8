# Critter Caretaker
# A virtual pet to care for

import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = random.randint(0,10)
        self.boredom = random.randint(0,10)

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
    #Added client inputted food variable to change how much food
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

    def destroy_stupid_user(self):
        print("GRAAAH!!!! you are so STUPID!")
        print("\n\n your critter has mutated into")
        print("a giant OMEGA SQUIRREL. And it has")
        print("eaten you.")
        print("\n\nNext time, follow directions!")
    def hidden(self):
        print("Critter name: " + self.name)
        print("Boredom: " + str(self.boredom))
        print("Mood: " + self.mood)
        print("Hunger: " + str(self.hunger))


def main():
    crit_name = input("What do you want to name your 1st critter?: ")
    crit2_name = input("What do you want to name your 2nd critter?: ")
    crit3_name = input("What do you want to name your 3rd critter?: ")
    crit = Critter(crit_name)
    crit2 = Critter(crit2_name)
    crit3 = Critter(crit3_name)


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

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
            crit2.talk()
            crit3.talk()
        # feed your critter
        elif choice == "2":
            food = int(input("Enter grams of food to feed critter: ")) # Get how much food
            crit.eat(food)
            crit2.eat(food)
            crit3.eat(food)
        # play with your critter
        elif choice == "3":
            fun = int(input('Enter how long to play with critter: '))
            crit.play(fun)
            crit2.play(fun)
            crit3.play(fun)

        #Hidden method
        elif choice == "Secret":
            crit.hidden()
            crit2.hidden()
            crit3.hidden()
            
        # some unknown choice
        else:
            crit.destroy_stupid_user()


main()
input("\n\nPress the enter key to exit.") 
