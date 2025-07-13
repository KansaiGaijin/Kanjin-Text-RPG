import time
import sys
sys.path.append('.')

from player import Player # Only import what's necessary
from enum_list import ItemType, Slots
from race_list import Elf, Dwarf, Human
from job_list import Barbarian, Cleric, Wizard


def wait():
    input("Press enter to continue...")

def startGame():
    print("Welcome stranger, to the world of Kanjin!.")
    start = input("Would you like to create your own character or use pre-generated stats?"
                  "\n 1) Create a new character\n 2) Pre-generated\n >> ")
    while True:
        if start in ("1", "Create"):
            while True:  # Global check to see if Name, Age, and Gender are correct
                # Name
                name = input('What is your name?\n >> ').title()
                while len(name) < 2:
                    name = input('Name must be longer than one character. Try again.\nWhat is your name?\n >> ')
                # Gender
                while True:
                    gender_select = input("What is your gender?\n"
                                          "1) Male\n2) Female\n3) Other\n >> ")
                    if gender_select not in ("male", "female", "other", "1", "2", "3"):
                        print("Sorry I didn't recognise that gender. Please try again.")
                        continue
                    else:
                        break
                if gender_select in ("1", "male"):
                    gender = "Male"
                elif gender_select in ("2", "female"):
                    gender = "Female"
                elif gender_select in ("3", "other"):
                    gender = "Other"
                # Age
                while True:
                    try:
                        age = int(input('How old are you?\n >> '))
                        break
                    except ValueError:
                        print("Sorry I didn't recognise that age. Please type in a whole number.")
                        continue
                # Double check responses
                correct = input(f"Hello, {name}. You are a {age} year old {gender}.\nIs this correct? Y/N\n >> ")
                if correct in ['y', 'yes']:
                    break
                elif correct in ['n', 'no']:
                    continue
                else:
                    print("Sorry, I didn't catch that.\n")
                    correct = input(f"You are a {age} year old {gender}. \nIs this correct? Y/N\n >> ")
                    if correct in ['y', 'yes']:
                        break
                    elif correct in ['n', 'no']:
                        continue
                break

            race = None
            job = None

            while True:  # Global check to see if Race and Job are correct
                # Race
                selected_race_obj = None
                while True:
                    race_choice = input("Please select a race to learn more about it:\n"
                                        "1) Elf\n2) Dwarf\n3) Human\n >> ").title()
                    if race_choice in ['Elf', '1']:
                        selected_race_obj = Elf
                    elif race_choice in ['Dwarf', '2']:
                        selected_race_obj = Dwarf
                    elif race_choice in ['Human', '3']:
                        selected_race_obj = Human
                    else:
                        print("Sorry I didn't recognise that race. Please select 'Elf', 'Dwarf', or 'Human'.\n")
                        continue

                    if selected_race_obj:
                        print(f"\n--- {selected_race_obj.name} ---")
                        print(selected_race_obj.__repr__())  # Use the __repr__ to get full description and traits
                    print('Would you like to proceed with this race or view another?')
                    proceed = input('1) Proceed\n2) View another race\n >> ')
                    if proceed in ('1', 'proceed'):
                        race = selected_race_obj
                        break
                    elif proceed in ('2', 'view', 'view another', 'view another race'):
                        race = None
                        continue
                # Job
                selected_job_obj = None
                while True:
                    job_choice = input("Please select a race to learn more about it:\n"
                                        "1) Barbarian\n2) Cleric\n3) Wizard\n >> ").title()
                    if job_choice in ['Barbarian', '1']:
                        selected_job_obj = Barbarian
                    elif job_choice in ['Cleric', '2']:
                        selected_job_obj = Cleric
                    elif job_choice in ['Wizard', '3']:
                        selected_job_obj = Wizard
                    else:
                        print("Sorry I didn't recognise that job. Please select 'Barbarian', 'Cleric', or 'Wizard'.\n")
                        continue

                    if selected_job_obj:
                        print(f"\n--- {selected_job_obj.name} ---")
                        print(selected_job_obj.__repr__())  # Use the __repr__ to get full description and traits

                    print('Would you like to proceed with this job or view another?')
                    proceed = input('1) Proceed\n2) View another job\n >> ')
                    if proceed in ('1', 'proceed'):
                        job = selected_job_obj  # Store the string name
                        break
                    elif proceed in ('2', 'view', 'view another', 'view another job'):
                        job = None
                        continue
                    else:
                        print("Sorry, I didn't catch that. Please try again.\n")

                # Final check
                while True:
                    correct = input(f"{name}, you are a {race.name_adjective} {job.name}.\nIs this correct? Y/N\n >> ")
                    if correct in ['y', 'yes']:
                        break
                    elif correct in ['n', 'no']:
                        continue
                    else:
                        print("Sorry, I didn't catch that. Please try again.\n")
                        continue
                return name, gender, age, race, job
        elif start in ("2", "pre-generated"):
            print("Please be prepared to enter a name, gender, age, race, and class, from those available in the game."
                  "\nIf you are unsure what the options are, please go back and create a new character.")
            create = input("Do you wish to continue? Y/N\n >> ").lower()
            if create in ("y", "yes"):
                name = input("Name: ")
                gender = input("Gender: ")
                age = int(input("Age: "))
                race = input("Race: ")
                job = input("Job: ")
                return name, gender, age, race, job  # Return and exit function
            elif create in ("n", "no"):
                # If 'n', continue the outer while True loop to re-prompt the initial choice.
                continue
            else:
                print("Invalid input. Please enter Y or N.")
                # If invalid, continue the outer while True loop to re-prompt the initial choice.
                continue
        else:
            print("Invalid input. Please select '1' or '2'.")
            # Continue the outer while True loop to re-prompt the initial choice.
            continue

def query_equip(player: Player):
    """Allows the player to view or change equipped items."""
    while True:
        print("Do you want to:\n"
              "1) View your equipped items\n"
              "2) Change your equipped items\n"
              "3) Return")
        response = input(">> ")
        if response == "1":
            player.inventory.current_equipment()
        elif response == "2":
            change_equip(player)
        elif response == "3":
            break

def change_equip(player: Player):
    """Handles the process of changing equipped items."""
    player.inventory.update_attunement() # Ensure attunement is up-to-date
    while True:
        response = input("Which equipment slot would you like to change?\n"
                         "1) Weapon\n"
                         "2) Armor\n"
                         "3) Other\n"
                         "4) Return\n"
                         ">> ").title()

        if response in ("1", "Weapon"):
            # Filter weapons from inventory that are not currently equipped in weapon slots
            itemlist = [item_obj for item_obj, item_data in player.inventory.items.items()
                        if item_data["object"] == ItemType.Weapon and
                        item_obj not in [player.inventory.equipped_items[Slots.MainHand],
                                         player.inventory.equipped_items[Slots.OffHand],
                                         player.inventory.equipped_items[Slots.TwoHanded]]]
            itemlist.append("Return") # Add return option last

            if not itemlist or (len(itemlist) == 1 and itemlist[0] == "Return"):
                print("You have no unequipped weapons available in your inventory.\n")
            else:
                print("What would you like to equip?\n")
                for i, item_obj in enumerate(itemlist, start=1):
                    if item_obj == "Return":
                        print(f'{i}) {item_obj}')
                    else:
                        print(f'{i}) {item_obj.name}')

                try:
                    selection = int(input(">> "))
                    if 1 <= selection <= len(itemlist):
                        chosen_item = itemlist[selection - 1]
                        if chosen_item == "Return":
                            break
                        else:
                            # Determine the correct slot based on weapon type
                            if chosen_item.slot == Slots.TwoHanded:
                                player.inventory.equip_item(chosen_item, Slots.TwoHanded)
                            elif chosen_item.versatile: # For versatile, equip to main hand
                                player.inventory.equip_item(chosen_item, Slots.MainHand)
                            else: # Default to main hand for 1H weapons
                                player.inventory.equip_item(chosen_item, Slots.MainHand)
                            player.inventory.current_equipment()
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif response in ("2", "Armor"):
            itemlist = [item_obj for item_obj, item_data in player.inventory.items.items()
                        if item_data["object"] == ItemType.Armor and
                        item_obj not in [player.inventory.equipped_items[Slots.Helm],
                                         player.inventory.equipped_items[Slots.Chest],
                                         player.inventory.equipped_items[Slots.Wrists],
                                         player.inventory.equipped_items[Slots.Feet]]]
            itemlist.append("Return")

            if not itemlist or (len(itemlist) == 1 and itemlist[0] == "Return"):
                print("You have no unequipped armor available in your inventory.\n")
            else:
                print("What would you like to equip?\n")
                for i, item_obj in enumerate(itemlist, start=1):
                    if item_obj == "Return":
                        print(f'{i}) {item_obj}')
                    else:
                        print(f'{i}) {item_obj.name}')

                try:
                    selection = int(input(">> "))
                    if 1 <= selection <= len(itemlist):
                        chosen_item = itemlist[selection - 1]
                        if chosen_item == "Return":
                            break
                        else:
                            # Logic for equipping armor based on its intended slot
                            if chosen_item.slot == Slots.Helm:
                                player.inventory.equip_item(chosen_item, Slots.Helm)
                            elif chosen_item.slot == Slots.Chest:
                                player.inventory.equip_item(chosen_item, Slots.Chest)
                            elif chosen_item.slot == Slots.Wrists:
                                player.inventory.equip_item(chosen_item, Slots.Wrists)
                            elif chosen_item.slot == Slots.Feet:
                                player.inventory.equip_item(chosen_item, Slots.Feet)
                            else:
                                print(f"This armor ({chosen_item.name}) doesn't seem to fit a standard slot.")
                            player.inventory.current_equipment()
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif response in ("3", "Other"):
            itemlist = [item_obj for item_obj, item_data in player.inventory.items.items()
                        if item_data["object"] == ItemType.Item and
                        item_obj not in [player.inventory.equipped_items[Slots.Neck],
                                         player.inventory.equipped_items[Slots.Cloak],
                                         player.inventory.equipped_items[Slots.LeftRing],
                                         player.inventory.equipped_items[Slots.RightRing],
                                         player.inventory.equipped_items[Slots.Other]]]
            itemlist.append("Return")

            if not itemlist or (len(itemlist) == 1 and itemlist[0] == "Return"):
                print("You have no other unequipped items available in your inventory.\n")
            else:
                print("What would you like to equip?\n")
                for i, item_obj in enumerate(itemlist, start=1):
                    if item_obj == "Return":
                        print(f'{i}) {item_obj}')
                    else:
                        print(f'{i}) {item_obj.name}')

                try:
                    selection = int(input(">> "))
                    if 1 <= selection <= len(itemlist):
                        chosen_item = itemlist[selection - 1]
                        if chosen_item == "Return":
                            break
                        else:
                            # Logic for equipping other items based on their intended slot
                            if chosen_item.slot == Slots.Neck:
                                player.inventory.equip_item(chosen_item, Slots.Neck)
                            elif chosen_item.slot == Slots.Cloak:
                                player.inventory.equip_item(chosen_item, Slots.Cloak)
                            elif chosen_item.slot == Slots.LeftRing:
                                player.inventory.equip_item(chosen_item, Slots.LeftRing)
                            elif chosen_item.slot == Slots.RightRing:
                                player.inventory.equip_item(chosen_item, Slots.RightRing)
                            elif chosen_item.slot == Slots.Other:
                                player.inventory.equip_item(chosen_item, Slots.Other)
                            else:
                                print(f"This item ({chosen_item.name}) doesn't seem to fit a standard 'other' slot.")
                            player.inventory.current_equipment()
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif response in ("4", "Return"):
            break
        else:
            print("That wasn't an option.")


def get_instructions():
    descrip1 = ("There are certain commands that will be available almost anytime you are able to type,\n"
                "such as viewing your inventory, checking your equipped items, and also changing them.\n"
                "You can also view your stats including your current and max hp.\n")
    descrip2 = ("Some examples are: 'Check inventory', 'Check equipment', and 'View stats'.\n"
                "To travel to a new area, just type 'Go north' or 'enter cave' etc.\n"
                "To replay the description of the current area, type 'location'.")
    print(descrip1)
    time.sleep(1) # Reduced sleep for faster testing
    print(descrip2)


def error_message():
    print("That command was not recognised. Please try again.")


def parse(input_text):
    command = input_text.lower()
    object1 = None
    remaining_words_index = None
    words = input_text.split()

    if not words: # Handle empty input
        return "error", None

    # Check for multi-word commands first to avoid partial matches
    if len(words) >= 2:
        if words[0] == "check" and words[1] in ("inventory", "bag", "backpack"):
            command = "inventory"
            return command, object1
        elif words[0] == "check" and words[1] in ("equipment", "equip", "items"):
            command = "equipment"
            return command, object1
        elif words[0] == "check" and words[1] == "stats":
            command = "stats"
            return command, object1
        elif words[0] == "check" and words[1] in ("hp", "hitpoints", "health"):
            command = "hp"
            return command, object1
        elif words[0] == "go":
            command = "go"
            object1 = " ".join(words[1:]) # The rest of the words are the direction
            return command, object1
        elif words[0] == "pick" and words[1] == "up" and len(words) > 2:
            command = "take"
            object1 = " ".join(words[2:])
            return command, object1

    # Single-word commands
    if words[0] == "help":
        command = "help"
    elif words[0] == "scene" or words[0] == "location": # Added 'location' as an alias
        command = "scene"
    elif words[0] in ("inventory", "bag", "backpack"):
        command = "inventory"
    elif words[0] in ("equip", "equipment"):
        command = "equipment"
    elif words[0] == "stats":
        command = "stats"
    elif words[0] in ("hp", "hitpoints", "health"):
        command = "hp"
    elif words[0] == "examine":
        if len(words) > 1:
            command = "examine"
            object1 = " ".join(words[1:])
        else:
            command = "examine" # User needs to specify what to examine
            object1 = None
    elif words[0] == "take":
        if len(words) > 1:
            command = "take"
            object1 = " ".join(words[1:])
        else:
            command = "take" # User needs to specify what to take
            object1 = None
    elif words[0] == "loot":
        if len(words) > 1:
            command = "loot"
            object1 = " ".join(words[1:])
        else:
            command = "loot" # User needs to specify what to loot
            object1 = None
    elif words[0] == "drop":
        if len(words) > 1:
            command = "drop"
            object1 = " ".join(words[1:])
        else:
            command = "drop" # User needs to specify what to drop
            object1 = None
    elif words[0] == "quit":
        command = "quit"
    else:
        command = "error" # Default for unrecognized commands

    return command, object1

# def skill_check(skill):
#     """Roll a d20 and add modifier
#     Return value to compare vs a hardcoded DC"""
#
#
# def roll_dice(num_dice):
#     roll_results = []
#     for _ in range(num_dice):
#         roll = randint(*user.hitDie)
#         roll_results.append(roll)
#         return roll_results


def calc_weight():
    pass # Placeholder for future weight calculation
