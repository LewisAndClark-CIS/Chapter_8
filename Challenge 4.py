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

    crit1 = Critter(input("What do you want to name your critter?: "))
    farm = [crit1]

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to a pet
        2 - Feed a pet
        3 - Play with a pets
        4 - Add another pet
        5 - Feed all pets
        6 - Play with all pets
        7 - Listen to all pets
        """)

        choice = input("Choice: ")
        print()
        count = 1
        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            sub = int(input('what number pet do you want to listen to?'))
            while sub not in range(len(farm)):
                print ('please input a number between 0 and', (len(farm) - 1), end = '')
                sub = int(input(' '))

            farm[sub].talk()

        # feed your critter
        elif choice == "2":

            sub = int(input('what number pet do you want to feed'))
            while sub not in range(len(farm)):
                print ('please input a number between 0 and', (len(farm) - 1), end = '')
                sub = int(input(' '))
            farm[sub].eat()

        # play with your critter
        elif choice == "3":
            sub = int(input('what number pet do you want to play with'))
            while sub not in range(len(farm)):
                print ('please input a number between 0 and', (len(farm) - 1), end = '')
                sub = int(input(' '))
            farm[sub].play()

        elif choice == "4":
            count += 1
            if count == 2:
                crit2 = Critter(input("What do you want to name your critter?: "))
                farm.append(crit2)
            elif count == 3:
                crit3 = Critter(input("What do you want to name your critter?: "))
                farm.append(crit3)
            elif count == 4:
                crit4 = Critter(input("What do you want to name your critter?: "))
                farm.append(crit4)
            elif count == 5:
                crit5 = Critter(input("What do you want to name your critter?: "))
                farm.append(crit5)
            elif count == 6:
                crit6 = Critter(input("What do you want to name your critter?: "))
                farm.append(crit6)
            else:
                print ('sorry your farm is not big enough to add any more pets')

        elif choice == "5":
            for i in farm:
                i.eat()
        elif choice == "6":
            for i in farm:
                i.play()

        elif choice == "7":
            for i in farm:
                i.talk()


        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
