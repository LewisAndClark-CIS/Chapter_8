class Critter(object):
    """A Virtual Pet"""

    total = 0

    def __init__(self, name, hunger=0, boredom=0):
        print("A new critter has been born!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("I am", self.name, "and I feel", self.mood, "now")
        self.__pass_time()

    def eat(self, food=4):
        foodAmount = int(input("How much food: "))
        print("Brruppp. Thank you.")
        self.hunger -= foodAmount
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        playTime = int(input("How long: "))
        print("Wheee!")
        self.boredom -= playTime
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

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


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None

    while choice != "0":
        print("""
            Critter Caretaker

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """)
        choice = input("Choice: ")
        print()

        #Exit
        if choice == "0":
            print("Good-bye.")

        #Listen
        elif choice == "1":
            crit.talk()
        #Eat
        elif choice == "2":
            crit.eat()
        #Play
        elif choice == "3":
            crit.play()

main()