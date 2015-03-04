#Critter Caretaker
#A virtual pet to care for

class Farm(object):
    def talk(self, farm):
        farm.talk()

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    # __ denotes private method
    def __pass_time(self, farm):
        self.hunger += 1
        self.boredom += 1
        self.__str__()

    def __str__(self, farm):
        print("Hunger is", self.hunger, "Boredom is ", self.boredom)
        print("Unhappiness is ", self.hunger + self.boredom, "and Mood is ", self.mood)

    @property
    def mood(self, farm):
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

    def talk(self, farm):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, farm):
        food = int(input("Enter how much food to feed your critter: "))
        print("Brruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, farm):
        fun = int(input("Enter how much fun you want your critter to have: "))
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    crit1 = Critter("Jessie")
    crit2 = Critter("Bob")
    farm = [crit1, crit2]

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
            print("Good-bye!")

        elif choice == "1":
            self.talk()

        elif choice == "2":
            crit.eat()

        elif choice == "3":
            crit.play()

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")
            
            
