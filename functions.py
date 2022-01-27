import time


def wait():
    input("Press enter to continue...")


# start game
def startGame():
    print("Welcome, stranger.")
    while True:
        # Name
        name = input("\n" + "What is your name?" + "\n" + ">> ").title()
        # Gender
        gender = input("What is your gender? Male, Female, or Other." + "\n" + ">> ").lower()
        while True:
            if gender not in ("male", "female", "other"):
                print("Sorry I didn't recognise that gender. Please select 'Male', 'Female', or 'Other'.")
                gender = input("\n" + ">> ").lower()
            else:
                break
        while True:
            # Age
            try:
                age = input("How old are you?" + "\n" + ">> ")
                age = int(age)
                break
            except ValueError:
                print("Sorry I didn't recognise that age. Please type in a whole number.")
                continue
        # Double check responses
        correct = input(f"Hello, {name}. You are a {age} year old {gender}.\nIs this correct? Y/N\n>> ").lower()
        if correct in ['y', 'yes']:
            break
        elif correct in ['n', 'no']:
            continue
        else:
            print("Sorry, I didn't catch that.\n")
            correct = input(f"You are a {age} year old {gender}. \nIs this correct? Y/N\n>> ").lower()
            if correct in ['y', 'yes']:
                break
            elif correct in ['n', 'no']:
                continue
    while True:
        # Race
        race = input("Please select a race from: Human, Elf, or Dwarf.\n>> ").title()
        while True:
            if race.lower() not in ("human", "elf", "dwarf"):
                race = input("Sorry I didn't recognise that race. Please select 'Human', "
                             "'Elf', or 'Dwarf'.\n>> ").title()
            else:
                break
        # Job
        job = input("Please select a class from: Warrior, Ranger, or Mage.\n>> ").lower()
        while True:
            if job not in ("warrior", "ranger", "mage"):
                job = input("Sorry I didn't recognise that class. Please select 'Warrior', 'Ranger', or 'Mage'.\n>> ")
            else:
                break
        # Final check
        correct = input(f"{name}, you are a {race} {job}.\nIs this correct? Y/N\n>> ").lower()
        if correct in ['y', 'yes']:
            break
        elif correct in ['n', 'no']:
            continue
        else:
            print("Sorry, I didn't catch that.\n")
            correct = input(f"You are a {race} {job}. \nIs this correct? Y/N\n>> ").lower()
            if correct in ['y', 'yes']:
                break
            elif correct in ['n', 'no']:
                continue
    return name, gender, age, race, job


def query_equip():
    print("Do you want to:\n"
          "1) View your equipped items\n"
          "2) Change your equipped items")
    response = input(">> ")
    if response == "1":
        return "view"
    elif response == "2":
        return "change"


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


# Receive action input
# Under development
def parse(input_text):
    command = input_text.lower()
    object1 = None

    # the .split() function splits the input_text string into a list of individual words
    words = input_text.split()

    if len(words) > 0:
        if words[0] == "help":
            command = "help"

        if words[0] == "inventory":
            command = "inventory"

        if words[0] == "equip" or words[0] == "equipment":
            command = "equipment"

        # found_examine_words = False
        # remaining_words_index = 0
        # if words[0] == "examine" or words[0] == "inspect" or words[0] == "study":
        #     remaining_words_index = 1
        #     found_examine_words = True
        # if words[0] == "look" and words[1] == "at":
        #     remaining_words_index = 2
        #     found_examine_words = True
        #
        # if found_examine_words:
        #     if len(words) > remaining_words_index:
        #         remaining_words = ""
        #         for i in range(remaining_words_index, len(words)):
        #             remaining_words += words[i]
        #             if i < len(words)-1:
        #                 remaining_words += " "
        #         command = "examine"
        #         object1 = remaining_words
        #
        # found_take_words = False
        # if (words[0] == "take") and len(words) > 1:
        #     found_take_words = True
        #     remaining_words_index = 1
        #
        # if (words[0] == "pick") and (words[1] == "up") and len(words) > 2:
        #     found_take_words = True
        #     remaining_words_index = 1
        #
        # if found_take_words:
        #     remaining_words = ""
        #     for i in range(remaining_words_index, len(words)):
        #         remaining_words += words[i]
        #         if i < len(words) - 1:
        #             remaining_words += " "
        #     command = "take"
        #     object1 = remaining_words

    return command, object1
