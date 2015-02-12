# Critter Caretaker
# Colaboration on Chapter 8 with Sam Coon and Tyler Kapusniak
# A virtual pet to care for

class CritterOne(object):
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
        food = int(input("How much food do you want to give to " + self.name + "?(lbs) "))
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 0):
        fun = int(input("How long do you want to play with " + self.name + "?(minutes) "))
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def secret(self):
        unhappiness = self.hunger + self.boredom
        print("Critter name: " + self.name)
        print("Unhappiness:", unhappiness)
        print("Hunger:", self.hunger)
        print("Boredom:", self.boredom)
        self.__pass_time()

class CritterTwo(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 6, boredom = 3):
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
    
    def eat(self, food = 5):
        food = int(input("How much food do you want to give to " + self.name + "?(lbs) "))
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 0):
        fun = int(input("How long do you want to play with " + self.name + "?(minutes) "))
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def secret(self):
        unhappiness = self.hunger + self.boredom
        print("Critter name: " + self.name)
        print("Unhappiness:", unhappiness)
        print("Hunger:", self.hunger)
        print("Boredom:", self.boredom)
        self.__pass_time()

class CritterThree(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 2, boredom = 7):
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
    
    def eat(self, food = 5):
        food = int(input("How much food do you want to give to " + self.name + "?(lbs) "))
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 0):
        fun = int(input("How long do you want to play with " + self.name + "?(minutes) "))
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def secret(self):
        unhappiness = self.hunger + self.boredom
        print("Critter name: " + self.name)
        print("Unhappiness:", unhappiness)
        print("Hunger:", self.hunger)
        print("Boredom:", self.boredom)
        self.__pass_time()

def main():
    crit1_name = input("What do you want to name your critter?: ")
    crit1 = CritterOne(crit1_name)
    crit2_name = input("What do you want to name your second critter?: ")
    crit2 = CritterTwo(crit2_name)
    crit3_name = input("What do you want to name your third critter?: ")
    crit3 = CritterThree(crit3_name)

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
            crit1.talk()
            crit2.talk()
            crit3.talk()
        
        # feed your critter
        elif choice == "2":
            crit1.eat()
            crit2.eat()
            crit3.eat()
         
        # play with your critter
        elif choice == "3":
            crit1.play()
            crit2.play()
            crit3.play()

        # secret
        elif choice == "4":
            crit1.secret()
            crit2.secret()
            crit3.secret()
            
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
