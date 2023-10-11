"""
Author: Sierra Brightly
Date: 10/2/2023
Title: Project 1 Part 2

Description: 
A Program with a menu that interacts with one of the components from Part 1
of Project 1 and does the following: 

1. Instantiates an object from a class that you write that has attributes 
and behaviors reflecting your design,gets basic input from a user that 
fills in the attributes of your object,

2. Displays basic info about your object and its behaviors.

3. A menu item that allows the user to quit the program; saying goodbye when 
selected, looping back to the menu after finishing an item (other than quitting)

Note: I decided to do this character different than what was mentioned in part 1. I
would like to build upon Part 1 as I move on, but I'm not quite there yet with skills.
 

Tests that could be ran: 

1. Set character information with different choices and verify that the character's 
information is correctly displayed. 

2. Test the roll_stat method by rolling many times and ensure that the rolls are 
between 3 and 18. Verify that modifiers are correct based on backstory.

3. Input invalid options for race, class, backstory, or menu selections.

"""

import random

class Character:
    """Represents a Character object."""

    def __init__(self):
        """Initialize a Character."""

        self.name = ""
        self.race = ""
        self.char_class = ""
        self.backstory = ""
        self.movement = 0
        self.base_health = 0
        self.brawns_rolls = []
        self.brains_rolls = []
        self.cool_rolls = []
        self.brawns = 0
        self.brains = 0
        self.cool = 0

    def set_character_info(self):
        """Sets character information and stats."""

        #Enter a name
        self.name = input("Enter character's name: ")
        
        # Choose a race
        while True:
            print("\nChoose a race:")
            print("1. Human (Movement: 30)")
            print("2. Elf (Movement: 35)")
            print("3. Dwarf (Movement: 25)")
            race_choice = input("Enter the number of your chosen race: ")
            if race_choice == "1":
                self.race = "Human"
                break
            elif race_choice == "2":
                self.race = "Elf"
                break
            elif race_choice == "3":
                self.race = "Dwarf"
                break
            else:
                print("\nInvalid option. Please choose again.")
        
        # Choose a class
        while True:
            print("\nChoose a class:")
            print("1. Warrior (Health: 100)")
            print("2. Mage (Health: 80)")
            print("3. Rogue (Health: 90)")
            class_choice = input("Enter the number of your chosen class: ")
            if class_choice == "1":
                self.char_class = "Warrior"
                break
            elif class_choice == "2":
                self.char_class = "Mage"
                break
            elif class_choice == "3":
                self.char_class = "Rogue"
                break
            else:
                print("\nInvalid option. Please choose again.")
        
        # Choose a backstory
        print("\nChoose a backstory:")
        while True:
            print("1. Pro Wrestler (Adds 2 points to Brawns)")
            print("2. Studious Student (Adds 2 points to Brains)")
            print("3. Sneaky Rapscallion (Adds 2 points to Coolness)")
            backstory_choice = input("Enter the number of your chosen backstory: ")
            if backstory_choice == "1":
                self.backstory = "Pro Wrestler"
                self.brawns += 2
                break
            elif backstory_choice == "2":
                self.backstory = "Studious Student"
                self.brains += 2
                break
            elif backstory_choice == "3":
                self.backstory = "Sneaky Rapscallion"
                self.cool += 2
                break
            else:
                print("\nInvalid option. Please choose again.")
        
        # Roll stats using 3d6 for each stat
        input("\nPress Enter to roll the dice for Brawns Stat.")
        self.roll_stat("Brawns")
        
        input("\nPress Enter to roll the dice for Brains Stat.")
        self.roll_stat("Brains")
        
        input("\nPress Enter to roll the dice for Coolness Stat.")
        self.roll_stat("Coolness")


    def roll_stat(self, stat_name):
        """Rolls 3d6 for a given stat and displays the result with modifiers."""

        rolls = [random.randint(1, 6) for _ in range(3)]
        total = sum(rolls)
        modifier = 0
        
        if stat_name == "Brawns":
            self.brawns_rolls = rolls
            self.brawns += total
            if self.backstory == "Pro Wrestler":
                modifier = 2
        elif stat_name == "Brains":
            self.brains_rolls = rolls
            self.brains += total
            if self.backstory == "Studious Student":
                modifier = 2
        elif stat_name == "Coolness":
            self.cool_rolls = rolls
            self.cool += total
            if self.backstory == "Sneaky Rapscallion":
                modifier = 2
        
        print(f"Dice Rolled: {', '.join(map(str, rolls))}")
        print(f"Modifier: +{modifier}")
        print(f"Total {stat_name}: {total + modifier}")

    def display_character_info(self):
        """Displays character information."""

        print("\nCharacter Information:")
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print(f"Movement: {self.movement}")
        print(f"Base Health: {self.base_health}")
        print(f"Brawns: {self.brawns}")
        print(f"Brains: {self.brains}")
        print(f"Coolness: {self.cool}")
        print(f"Backstory: {self.backstory}")
        
    def assign_race_class_stats(self):
        """Assigns movement and health based of race and class."""

        if self.race == "Human":
            self.movement = 30
            self.base_health = 90
        elif self.race == "Elf":
            self.movement = 35
            self.base_health = 90
        elif self.race == "Dwarf":
            self.movement = 25
            self.base_health = 90

        if self.char_class == "Warrior":
            self.movement += 0
            self.base_health += 10
        elif self.char_class == "Mage":
            self.movement += 0
            self.base_health -= 10
        elif self.char_class == "Rogue":
            self.movement += 0
            self.base_health += 0

def main():
    character = Character()
    while True:
        print("\nMenu:")
        print("1. Set Character Info (and Roll Stats)")
        print("2. Display Character Info")
        print("3. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            character.set_character_info()
            character.assign_race_class_stats()
            print("\nCharacter info and stats set.")
            input("\nPress anything to returnt to menu")
        elif choice == "2":
            character.display_character_info()
            input("\nPress anything to return to menu")
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


