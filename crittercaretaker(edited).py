#   Critter Caretaker
#   A virtual pet to watch over

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
            m= "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("MMMM! Thank you! So Tasty!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("WHEEEE! That was fun!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def backdoor(self):
        print("Hunger:", self.hunger, "Boredom:", self.boredom)

def quit():
    print("Good Bye!")

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
         4 - View Backdoor
         """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            food = input("How much food would you like to feed your critter? (0-10) ")
            try:
                food = int(food)
                
            except:
                food = 5
                
            else:
                if food not in range(0, 10):
                    food = 5
                    
            crit.eat(food)

        # play with your critter
        elif choice == "3":
            fun = input("How much would you like to play with your critter? (0-10) ")
            try:
                fun = int(fun)

            except:
                fun = 5

            else:
                if fun not in range(0, 10):
                    fun = 5
            crit.play(fun)

        elif choice == "4":
             crit.backdoor()

        #some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
