"""
File: Project 1 Version 2
Author: Sierra Brightly
Student ID: X00465282
Date:October 10, 2023

Description: 
A character creator for a RPG "Lite" style game. This is an updated version from
Project 1 and can now save characters. It also has a couple test functions/methods
to test functionality: 
1.  Tests if a backstory is rolling stats that are within acceptable limits
(Currently set to "Pro Wrestler").
2. to see if the race/class health/movement stats are correct (currently "elf"/"mage").

I'm only 82% sure I've implemented these correctly. 
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

    def save_character(self):
        """Saves the character to a file in alphabetical order by name."""
        
        # Create a dictionary with character information
        character_info = {
            "Name": self.name,
            "Race": self.race,
            "Class": self.char_class,
            "Movement": self.movement,
            "Base Health": self.base_health,
            "Brawns": self.brawns,
            "Brains": self.brains,
            "Coolness": self.cool,
            "Backstory": self.backstory
        }

        # Read existing character data from the file, if it exists
        existing_characters = []
        try:
            with open("characters.txt", "r") as file:
                lines = file.readlines()
                character_data = {}
                for line in lines:
                    line = line.strip()
                    if line:
                        key, value = line.split(": ", 1)  # Split only at the first colon
                        character_data[key] = value
                    else:
                        existing_characters.append(character_data)
                        character_data = {}
                if character_data:
                    existing_characters.append(character_data)  # Append the last character
        except FileNotFoundError:
            print("File not found")
            pass

        # Append the new character information to the list
        existing_characters.append(character_info)

        # Sort the characters alphabetically by name
        existing_characters.sort(key=lambda x: x["Name"])

        # Write the sorted characters back to the file
        with open("characters.txt", "w") as file:
            for character in existing_characters:
                for key, value in character.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

        print(f"Character '{self.name}' has been saved to the file.")

def main():
    character = Character()
    while True:
        print("\nMenu:")
        print("1. Create A Character")
        print("2. Display Current Character Info")
        print("3. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            character.set_character_info()
            character.assign_race_class_stats()
            print("\nCharacter info and stats set.")

            # Testing if rolling stats are within acceptable limits.
            try:
                test_roll_stat()
            except AssertionError as e:
                print("Test failed", e)

            save_choice = input("Do you want to save this character? (y/n): ")
            if save_choice.lower() == "y":
                character.save_character()
            elif save_choice.lower() != "n":
                print("Invalid input. Character not saved.")
            
            input("\nPress anything to return to the menu")
        elif choice == "2":
            character.display_character_info()
            
            # Testing race/class stats.
            try:
                test_race_class_stats()
            except AssertionError as e:
                print("Test failed", e)            

            input("\nPress anything to return to the menu")
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def test_roll_stat():
    """Tests to make sure that stats rolled are within acceptable limits"""

    character = Character()
    
    # Manually set the character's backstory to "Pro Wrestler" for testing
    character.backstory = "Pro Wrestler"

    # Roll stats with known values
    character.roll_stat("Brawns")
    character.roll_stat("Brains")
    character.roll_stat("Coolness")

    # Check the expected values after rolling with "Pro Wrestler" backstory
    assert character.brawns_rolls != []
    assert character.brains_rolls != []
    assert character.cool_rolls != []
    assert character.brawns >= 3 + 2  # 3d6 sum + 2 modifier
    assert character.brains >= 3  # 3d6 sum
    assert character.cool >= 3  # 3d6 sum

    print("\nTest passed: roll_stat method works correctly.\n")

def test_race_class_stats():
    """Tests to make sure that stats for race and class are correct"""

    character = Character()

    # Set the character's race and class
    character.race = "Elf"
    character.char_class = "Mage"

    # Call the method to assign stats
    character.assign_race_class_stats()

    # Check if movement and base health are set correctly
    assert character.movement == 35  # Elf's movement
    assert character.base_health == 80  # Mage's base health

    print("Test passed: assign_race_class_stats method works correctly.")

if __name__ == "__main__":
    main()

    test_roll_stat()
    test_race_class_stats()
