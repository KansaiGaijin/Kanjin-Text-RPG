import time
from job_list import Barbarian, Cleric, Wizard
from player import *
from race_list import Elf, Dwarf, Human


def wait():
    input("Press enter to continue...")


def startGame():
    print("Welcome, stranger.")
    while True:
        # Initialise age
        age = None
        # Name
        name = input(f'\nWhat is your name?\n >> ').title()
        while len(name) < 2:
            name = input(f'Input name was too short. Try again. \nWhat is your name?\n >> ').title()
        # Gender
        gender = None
        gender_select = input("What is your gender?\n"
                              "1) Male\n2) Female\n3) Other\n >> ").lower()
        while True:
            if gender_select not in ("male", "female", "other", "1", "2", "3"):
                print("Sorry I didn't recognise that gender. Please select from the following:\n"
                      "1) Male\n2) Female\n3) Other")
                gender_select = input(">> ").lower()
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
                age = input(f'How old are you?\n >> ')
                age = int(age)
                break
            except ValueError:
                print("Sorry I didn't recognise that age. Please type in a whole number.")
                continue
        # Double check responses
        correct = input(f"Hello, {name}. You are a {age} year old {gender}.\nIs this correct? Y/N\n >> ").lower()
        if correct in ['y', 'yes']:
            pass
        elif correct in ['n', 'no']:
            continue
        else:
            print("Sorry, I didn't catch that.\n")
            correct = input(f"You are a {age} year old {gender}. \nIs this correct? Y/N\n >> ").lower()
            if correct in ['y', 'yes']:
                break
            elif correct in ['n', 'no']:
                continue
        break
    while True:
        # Race
        race = input("Please select a race to learn more about it: Elf, Dwarf, or Human.\n >> ").title()
        while True:
            if race not in ("Elf", "Dwarf", "Human", None):
                race = input("Sorry I didn't recognise that race. "
                             "Please select 'Elf', 'Dwarf', or 'Human'.\n >> ").title()
            elif race is None:
                race = input("Please select a race to learn more about it: Elf, Dwarf, or Human.\n >> ").title()
                continue
            else:
                if race == "Elf":
                    print(Elf)
                elif race == "Dwarf":
                    print(Dwarf)
                elif race == "Human":
                    print(Human)
            print('Would you like to proceed with this race or view another?')
            proceed = input(f'1) Proceed\n2) View another race\n >> ').lower()
            if proceed in ('1', 'proceed'):
                break
            elif proceed in ('2', 'view', 'view another', 'view another race'):
                race = None
                continue
        # Job
        job = input("Please select a job to learn more about it: Barbarian, Cleric, or Wizard.\n >> ").title()
        while True:
            if job not in ("Barbarian", "Cleric", "Wizard", None):
                job = input("Sorry I didn't recognise that job. "
                            "Please select 'Barbarian', 'Cleric', or 'Wizard'.\n >> ").title()
            elif job is None:
                job = input("Please select a job to learn more about it: Barbarian, Cleric, or Wizard.\n >> ").title()
                continue
            else:
                if job == "Barbarian":
                    print(Barbarian)
                elif job == "Cleric":
                    print(Cleric)
                elif job == "Wizard":
                    print(Wizard)
            print('Would you like to proceed with this job or view another?')
            proceed = input(f'1) Proceed\n2) View another job\n >> ').lower()
            if proceed in ('1', 'proceed'):
                break
            elif proceed in ('2', 'view', 'view another', 'view another job'):
                job = None
                continue

        # Final check
        correct = input(f"{name}, you are a {race} {job}.\nIs this correct? Y/N\n >> ").lower()
        if correct in ['y', 'yes']:
            break
        elif correct in ['n', 'no']:
            continue
        else:
            print("Sorry, I didn't catch that.\n")
            correct = input(f"You are a {race} {job}. \nIs this correct? Y/N\n >> ").lower()
            if correct in ['y', 'yes']:
                break
            elif correct in ['n', 'no']:
                continue
    return name, gender, age, race, job


def startGame_PreGen():
    """Use this for when the player is familiar with class races and jobs."""


def query_equip():
    print("Do you want to:\n"
          "1) View your equipped items\n"
          "2) Change your equipped items - Weapons complete\n"
          "3) Return")
    response = input(">> ")
    if response == "1":
        return "view"
    elif response == "2":
        return "change"
    elif response == "3":
        return None


def change_equip():
    response = input("Which equipment slot would you like to change?\n"
                     "1) Weapon\n"
                     "2) Armor\n"
                     "3) Other\n"
                     "4) Return\n"
                     ">> ").title()
    if response not in ("1", "2", "3", "4", "Weapon", "Armor", "Other", "Return"):
        print("Sorry I didn't recognise that. Please try again.\n")
        change_equip()
    elif response == "1" or "Weapon":  # Weapon
        itemlist = []  # create blank list for items
        print(f"You currently have equipped: \n"
              f"{view_equippedweapon()}")

        for item_key, item_value in Inventory.items():  # item, attribute
            for key, value in item_value.items():  # attribute, stat
                if key == "object" and value == Weapon:  # if item = class `Weapon`
                    itemlist.append(item_key)
                    if item_key in Equipment.values():
                        itemlist.remove(item_key)

        print("What would you like to equip?\n")
        option = ""
        for i, name in enumerate(itemlist, start=1):
            option = f'{i}) {name}'
            print(option)

        selection = int(input(">> "))
        for i, name in enumerate(itemlist, start=1):
            if selection == i:
                if name.itemType == "Weapon":
                    if name.slot == Slots.MainHand:
                        equip = {"Main Hand": name}
                        Equipment.update(equip)
                    elif not name.versatile:
                        equip = {"Off Hand": name}
                        Equipment.update(equip)
                    else:
                        equip = {"Main Hand": None, "Off Hand": None, "Two Handed": name}
                        Equipment.update(equip)
            else:
                print("That wasn't an option.")
        print(f"You currently have equipped: \n"
              f"{view_equippedweapon()}")
    elif response == "2" or "Armor":
        pass
    elif response == "3" or "Other":
        pass
    elif response == "4" or "Return":
        pass


def view_equippedweapon():
    equipped = ""
    for slot, equipment in Equipment.items():
        if slot in ("Main Hand", "Off Hand", "Two Handed") and equipment is not None:
            equipped = equipped + f'{slot}: {equipment} \n'
            return equipped
        else:
            return "You have nothing equipped!"


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


def error_message():
    print("That command was not recognised. Please try again.")


def parse(input_text):
    command = input_text.lower()
    object1 = None
    remaining_words_index = None

    # the .split() function splits the input_text string into a list of individual words
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


def skill_check(skill):
    """Roll a d20 and add modifier
    Return value to compare vs a hardcoded DC"""


def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


def roll_dice(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = randint(*user.hitDie)
        roll_results.append(roll)
        return roll_results


def current_inventory():
    """Prints a list of items in your backpack that aren't equipped to your person."""
    print(f'In your rucksack you have:')
    for item_key, item_value in Inventory.items():  # string, dictionary
        if item_key not in Equipment.values():
            values = item_value.values()  # make a variable of all values
            values_list = list(values)  # turn variable into a list
            count_value = values_list[0]  # take the first value from list - why?
            print(f'{item_key.name} x {count_value}\n'
                  f'    {item_key.description}')


def current_equipment():
    """Prints a list of items that you have equipped in your slots."""
    print(f'You are currently wearing:')
    for item_key, item_value in Equipment.items():  # string, dictionary
        if item_value is not None:
            if item_value.itemType == ItemType.WEAPON:
                print(f'{item_key}: {item_value.name} - {item_value.damage1H}\n'
                      f'    {item_value.description}')
            elif item_value.itemType == ItemType.ARMOR:
                print(f'{item_key}: {item_value.name} - AC {item_value.ac}\n'
                      f'    {item_value.description}')


def calc_weight():
    pass
