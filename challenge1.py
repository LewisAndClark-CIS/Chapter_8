#Andrew Hecky
"""
1) Improve the critter caretaker program by allowing the user to specify how
much food he or she feeds the critter and how long he or she plays with the
critter. Have these values affect how quickly the critter's hunger and boredom
levels drop.
"""

class Critter(object):
    #A virtual pet
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
            m = "fine"
        elif 11 <= unhappiness <= 15:
            m = "upset"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        print(str("The critter's hunger is: " + self.hunger))
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        print("The critter's fun is: " + str(self.boredom))
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def error_encounter(self):
        print("Error encountered. Please select a valid option. ")
              
    def hidden(self):
        print("Critter name: " + self.name)
        print("Boredom: " + str(self.boredom))
        print("Mood: " + self.mood)
        print("Hunger: " + str(self.hunger))


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)
    crit2 = Critter("Fred")


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

        #Listen
        elif choice == "1":
            crit.talk()
        
        #Feed
        elif choice == "2":
            food = int(input("Enter grams of food to feed critter: ")) # Get how much food
            crit.eat(food)
         
        #Play
        elif choice == "3":
            fun = int(input('Enter how long to play with critter: '))
            crit.play(fun)


        #Hidden method
        elif choice == "Secret":
            crit.hidden()
            
        #Unknown 
        else:
            crit.error_encounter()
            #choice = "0"

main()
input("\n\nPress the enter key to exit.") 
