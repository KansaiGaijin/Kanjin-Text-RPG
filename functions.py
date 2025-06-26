import time

from player import *

def wait():
    input("Press enter to continue...")


def startGame():
    print("Welcome, stranger.")
    start = input("Would you like to create your own character or use pre-generated stats?"
                  "\n 1) Create a new character\n 2) Pre-generated\n >> ")
    while True:
        if start in ("2", "Pregen"):
            print("Please be prepared to enter a name, gender, age, race, and class, from those available in the game."
                     "\nIf you are unsure what the options are, please go back and create a new character.")
            create = input("Do you wish to continue? Y/N\n >> ")
            if create in ("y", "yes"):
                name = input("Name: ")
                gender = input("Gender: ")
                age = int(input("Age: ")
                race = input("Race: ")
                job = input("Job: ")
                return name, gender, age, race, job
            elif create in ("n", "no"):
                start = "1"
        elif start in ("1", "Create"):
            while True:  # Global check to see if Name, Age, and Gender are correct
                # Name
                name = input('What is your name?\n >> ')
                while len(name) < 2:
                    name = input('Input name was too short. Try again.\nWhat is your name?\n >> ')
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
                while True:
                    # Age
                    try:
                        age = int(input('How old are you?\n >> ')
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

            while True:  # Global check to see if Race and Job are correct
                # Race
                while True:
                    race = input("Please select a race to learn more about it: Elf, Dwarf, or Human.\n >> ")
                    if race not in ("Elf", "Dwarf", "Human", None):
                        race = input("Sorry I didn't recognise that race. Please select 'Elf', 'Dwarf', or 'Human'.\n >> ")
                    elif race is None:
                        race = input("Please select a race to learn more about it: Elf, Dwarf, or Human.\n >> ")
                        continue
                    else:
                        # Replace these prints with appropriate explanations for the web interface
                        if race == "Elf":
                            print("Information about Elves...")
                        elif race == "Dwarf":
                            print("Information about Dwarves...")
                        elif race == "Human":
                            print("Information about Humans...")
                    print('Would you like to proceed with this race or view another?')
                    proceed = input('1) Proceed\n2) View another race\n >> ')
                    if proceed in ('1', 'proceed'):
                        break
                    elif proceed in ('2', 'view', 'view another', 'view another race'):
                        race = None
                        continue
                # Job
                while True:
                    job = input("Please select a job to learn more about it: Barbarian, Cleric, or Wizard.\n >> ")
                    if job not in ("Barbarian", "Cleric", "Wizard", None):
                        job = input("Sorry I didn't recognise that job. Please select 'Barbarian', 'Cleric', or 'Wizard'.\n >> ")
                    elif job is None:
                        job = input("Please select a job to learn more about it: Barbarian, Cleric, or Wizard.\n >> ")
                        continue
                    else:
                        # Replace these prints with appropriate explanations for the web interface
                        if job == "Barbarian":
                            print("Information about Barbarians...")
                        elif job == "Cleric":
                            print("Information about Clerics...")
                        elif job == "Wizard":
                            print("Information about Wizards...")
                    print('Would you like to proceed with this job or view another?')
                    proceed = input('1) Proceed\n2) View another job\n >> ')
                    if proceed in ('1', 'proceed'):
                        break
                    elif proceed in ('2', 'view', 'view another', 'view another job'):
                        job = None
                        continue
                while True:
                    # Final check
                    correct = input(f"{name}, you are a {race} {job}.\nIs this correct? Y/N\n >> ")
                    if correct in ['y', 'yes']:
                        break
                    elif correct in ['n', 'no']:
                        continue
                    else:
                        print("Sorry, I didn't catch that. Please try again.\n")
                        continue
                return name, gender, age, race, job


def query_equip():
    while True:
        print("Do you want to:\n"
              "1) View your equipped items\n"
              "2) Change your equipped items\n"
              "3) Return")
        response = input(">> ")
        if response == "1":
            current_equipment()
        elif response == "2":
            change_equip()
        elif response == "3":
            break


def change_equip():
    canAddAttunement()
    while True:
        response = input("Which equipment slot would you like to change?\n"
                         "1) Weapon\n"
                         "2) Armor\n"
                         "3) Other\n"
                         "4) Return\n"
                         ">> ").title()
        if response not in ("1", "2", "3", "4", "Weapon", "Armor", "Other", "Return"):
            print("Sorry I didn't recognise that. Please try again.\n")
            change_equip()
        elif response in ("1", "Weapon"):  # Weapon
            itemlist = ["Return"]  # create blank list for items
            for item_key, item_value in Inventory.items():  # item, attribute
                for key, value in item_value.items():  # attribute, stat
                    if key == "object" and value == Weapon:  # if item = class `Weapon`
                        itemlist.append(item_key)
                        if item_key in Equipment.values():
                            itemlist.remove(item_key)
            if len(itemlist) == 1:
                print("You have nothing available to equip.\n")
            else:
                print("What would you like to equip?\n")
                for i, name in enumerate(itemlist, start=1):
                    option = f'{i}) {name}\n'
                    print(option)
                selection = int(input(">> "))
                for i, name in enumerate(itemlist, start=1):
                    if selection == i:
                        if name == "Return":
                            break
                        elif name.itemType == ItemType.Weapon:
                            if name.attunement:  # if item has attunement
                                if not canAddAttunement():  # check if can add another attuned item
                                    if Equipment["Main Hand"].attunement:  # if attune is max, check if swapped weapon is attuned
                                        if name.versatile:
                                            Equipment["Main Hand"] = name
                                            Equipment["Off Hand"] = name
                                        elif name.slot == "Main Hand":
                                            Equipment["Main Hand"] = name
                                            Equipment["Off Hand"] = None
                                        elif name.slot == "Two Handed":
                                            Equipment["Main Hand"] = None
                                            Equipment["Off Hand"] = None
                                            Equipment["Two Handed"] = name
                                    else:
                                        print("\n Cannot equip items: Too many attuned items equipped")  # if not attuned, it refuses the equip.
                                        break
                                else:  # If canAddAttunement = True
                                    if name.versatile:
                                        Equipment["Main Hand"] = name
                                        Equipment["Off Hand"] = name
                                    elif name.slot == "Main Hand":
                                        Equipment["Main Hand"] = name
                                        Equipment["Off Hand"] = None
                                    elif name.slot == "Two Handed":
                                        Equipment["Main Hand"] = None
                                        Equipment["Off Hand"] = None
                                        Equipment["Two Handed"] = name

                print(f"{current_equipment()}")
        elif response in ("2", "Armor"):  # Armor
            itemlist = ["Return"]  # create blank list for items
            for item_key, item_value in Inventory.items():  # item, attribute
                for key, value in item_value.items():  # attribute, stat
                    if key == "object" and value == Armor:  # if item = class `Weapon`
                        itemlist.append(item_key)  # Add item type to list
                        if item_key in Equipment.values():
                            itemlist.remove(item_key)  # remove from list if currently equipped -
                            # consider if holding multiple objects
            if len(itemlist) == 1:
                print("You have nothing available to equip.\n")
            else:
                print("What would you like to equip?\n")
                for i, name in enumerate(itemlist, start=1):
                    option = f'{i}) {name}'
                    print(option)
                selection = int(input(">> "))
                for i, name in enumerate(itemlist, start=1):
                    if selection == i:
                        if name == "Return":
                            break
                        elif name.itemType == Armor:
                            try:
                                if name.attunment:
                                    print("Not coded attunement yet")  # if item has attunement - check availability
                            except AttributeError:  # if no attunement
                                if name.slot == Slots.Helm:
                                    equip = {"Helm": name}
                                    Equipment.update(equip)
                                elif name.slot == Slots.Chest:
                                    equip = {"Chest": name}
                                    Equipment.update(equip)
                                elif name.slot == Slots.Wrists:
                                    equip = {"Wrists": name}
                                    Equipment.update(equip)
                                elif name.slot == Slots.Feet:
                                    equip = {"Feet": name}
                                    Equipment.update(equip)
                print(f"You now have equipped: \n"
                      f"{current_equipment()}")
        elif response in ("3", "Other"):  # Other
            itemlist = ["Return"]  # create blank list for items
            for item_key, item_value in Inventory.items():  # item, attribute
                for key, value in item_value.items():  # attribute, stat
                    if key == "object" and value == Armor:  # if item = class `Weapon`
                        itemlist.append(item_key)  # Add item type to list
                        if item_key in Equipment.values():
                            itemlist.remove(item_key)  # remove from list if currently equipped -
                            # consider if holding multiple objects
            if len(itemlist) == 1:
                print("You have nothing available to equip.\n")
            else:
                print("What would you like to equip?\n")
                for i, name in enumerate(itemlist, start=1):
                    option = f'{i}) {name}'
                    print(option)
                selection = int(input(">> "))
                for i, name in enumerate(itemlist, start=1):
                    if selection == i:
                        if name == "Return":
                            break
                        elif name.itemType == Armor:
                            try:
                                if name.attunment:
                                    print("Not coded attunement yet")  # if item has attunement - check availability
                            except AttributeError:  # if no attunement
                                if name.slot == Slots.Neck:
                                    equip = {"Neck": name}
                                    Equipment.update(equip)
                                elif name.slot == Slots.Cloak:
                                    equip = {"Cloak": name}
                                    Equipment.update(equip)
                                elif name.slot == Slots.LeftRing:
                                    equip = {"Left Ring": name}
                                    Equipment.update(equip)
                                elif name.slot == Slots.RightRing:
                                    equip = {"Right Ring": name}
                                    Equipment.update(equip)
                print(f"You now have equipped: \n"
                      f"{current_equipment()}")
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
    time.sleep(5)
    print(descrip2)


def canAddAttunement():
    attune = 0
    for slot, equipment in Equipment.items():
        if isinstance(equipment, Weapon):
            if equipment.attunement:
                attune += 1
    Equipment["Attunement"] = attune
    if attune > 3:
        return False
    else:
        return True


def error_message():
    print("That command was not recognised. Please try again.")


def parse(input_text):
    command = input_text.lower()
    object1 = None
    remaining_words_index = None
    words = input_text.split()

    if len(words) > 0:
        if words[0] == "help":
            command = "help"

        if words[0] == "scene":
            command = "scene"

        if words[0] in ("view", "check", "show"):
            if words[1] in ("inventory", "bag", "backpack"):
                command = "inventory"
            elif words[1] in ("equipment", "equip", "items"):
                command = "equipment"
            elif words[1] == "stats":
                command = "stats"
            elif words[1] in ("hp", "hitpoints", "health"):
                command = "hp"
            elif words[1] == "hit" and words[2] == "points":
                command = "hp"

        if words[0] in ("equip", "equipment"):
            command = "equipment"

        if words[0] in ("inventory", "bag", "backpack"):
            command = "inventory"

        found_examine_words = False
        if (words[0] == "examine") and len(words) > 1:
            found_examine_words = True
            remaining_words_index = 1

        if found_examine_words:
            remaining_words = ""
            for i in range(remaining_words_index, len(words)):
                remaining_words += words[i]
                if i < len(words) - 1:
                    remaining_words += " "
            command = "examine"
            object1 = remaining_words

        found_take_words = False
        if ((words[0] == "take") and len(words) > 1) or \
                ((words[0] == "pick") and (words[1] == "up") and len(words) > 2):
            found_take_words = True
            remaining_words_index = 1

        if found_take_words:
            remaining_words = ""
            for i in range(remaining_words_index, len(words)):
                remaining_words += words[i]
                if i < len(words) - 1:
                    remaining_words += " "
            command = "take"
            object1 = remaining_words

        found_loot_words = False
        if (words[0] == "loot") and len(words) > 1:
            found_loot_words = True
            remaining_words_index = 1

        if found_loot_words:
            remaining_words = ""
            for i in range(remaining_words_index, len(words)):
                remaining_words += words[i]
                if i < len(words) - 1:
                    remaining_words += " "
            command = "loot"
            object1 = remaining_words

        found_drop_words = False
        if (words[0] == "drop") and len(words) > 1:
            found_drop_words = True
            remaining_words_index = 1

        if found_drop_words:
            remaining_words = ""
            for i in range(remaining_words_index, len(words)):
                remaining_words += words[i]
                if i < len(words) - 1:
                    remaining_words += " "
            command = "drop"
            object1 = remaining_words

        if words[0] not in ("view", "check", "show", "loot", "examine", "take", "equip", "equipment", "inventory",
                            "bag", "backpack", "drop"):
            command = "error"

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


def current_inventory():
    """Prints a list of items in your backpack that aren't equipped to your person."""
    print(f'In your rucksack you have:')
    for item_key, item_value in Inventory.items():  # string, dictionary
        if item_key not in Equipment.values():
            values = item_value.values()  # make a variable of all values
            values_list = list(values)  # turn variable into a list
            count_value = values_list[0]  # take the first value from list - why?
            print(f'{item_key.name} x {count_value}\n'
                  f'    {item_key.description}\n')


def current_equipment():
    """Prints a list of items that you have equipped in your slots."""
    print(f'You are currently wearing:')
    for slot, equipment in Equipment.items():  # string, dictionary
        if equipment is not None:
            if slot == "Attunement":
                continue
            elif equipment.itemType == ItemType.Weapon:
                if equipment.versatile:
                    print(f'{slot}: {equipment.name} - {equipment.versatiledmg}\n'
                          f'    {equipment.description}\n')
                    continue
                elif equipment.damage1H is not None:
                    print(f'{slot}: {equipment.name} - {equipment.damage1H}\n'
                          f'    {equipment.description}\n')
                elif equipment.damage2H is not None:
                    print(f'{slot}: {equipment.name} - {equipment.damage2H}\n'
                          f'    {equipment.description}\n')
            elif equipment.itemType == ItemType.Armor:
                print(f'{slot}: {equipment.name} - AC {equipment.ac}\n'
                      f'    {equipment.description}\n')
            elif equipment.itemType == ItemType.Item:
                print(f'{slot}: {equipment.name}\n'
                      f'    {equipment.description}\n')


def calc_weight():
    pass
