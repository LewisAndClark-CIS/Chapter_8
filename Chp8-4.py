# Critter Program v1.3
# New update allows user to care for multiple critters
# Author: Alton Stillwell
# Date: 2/12/15
####################################################################
# define class and functions
class Critter(object):
    def __init__(self,name,hunger = 0, boredom = 0):
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
        print("I'm", self.name, "and I feel",self.mood,"now.\n")
        self.__pass_time()
    def eat(self,food = 4):
        food = int(input("How much food(1-4): "))
        if 1 <= food <= 4:
            print("Brruppp. Thank you.")
            self.hunger -= food
        else:
            print("Invalid food choice.")
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        fun = int(input("How long do you want to play(1-4): "))
        if 1 <= fun <= 4:
            print("Wheee!")
            self.boredom -= fun
        else:
            print("Invalid time choice.")
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def __str__(self):
        print("Name:",self.name)
        print("Hunger:",self.hunger)
        print("Boredom:",self.boredom)
        print("Unhappiness:", (self.hunger + self.boredom))
        unhappiness = (self.hunger + self.boredom)
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        print("Mood:", m)
        print("~~~~~~~~~~~~~~~")
# main program loop
def main():
    crit_name = input("What is your first critters name? ")
    crit1 = Critter(crit_name)
    crit_name = input("What is your second critters name? ")
    crit2 = Critter(crit_name)
    crit_name = input("What is your third critters name? ")
    crit3 = Critter(crit_name)
    crit_name = input("What is your fourth critters name? ")
    crit4 = Critter(crit_name)
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
            print("Good-bye")
        elif choice == "1":
            crit1.talk()
            crit2.talk()
            crit3.talk()
            crit4.talk()
        elif choice == "2":
            crit1.eat()
            crit2.eat()
            crit3.eat()
            crit4.eat()
        elif choice == "3":
            crit1.play()
            crit2.play()
            crit3.play()
            crit4.play()
        elif choice == "A":
            crit1.__str__()
            crit2.__str__()
            crit3.__str__()
            crit4.__str__()
        else:
            print("\nSorry, but",choice,"isn't a valid choice.")
##################################################################
# call main program
main()
# exit text
("\n\nPress the <enter> key to exit.")
#################################################################
