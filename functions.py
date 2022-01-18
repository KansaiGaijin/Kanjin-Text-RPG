import time
import sys
from random import randint


def typingPrint(text, time, end='\n'):
    for character in text:
        print(character, end="")
        time.sleep(0.09)
        sys.stdout.flush()
    if end:
        print(end, end='')


def typingInput(text, time, end='\n'):
    for character in text:
        print(character, end="")
        time.sleep(0.09)
    if end:
        print(end, end='')
    value = input()
    return value


# start game
def startGame():
    typingPrint("Welcome, stranger.")
    while True:
        # Name
        name = typingInput("\n" + "What is your name?" + "\n" + ">> ", time).title()
        # Gender
        gender = typingInput("What is your gender? Male, Female, or Other." + "\n" + ">> ", time)
        while True:
            if gender.lower() not in ("male", "female", "other"):
                typingPrint("Sorry I didn't recognise that gender. Please select 'Male', 'Female', or 'Other'.", time)
                gender = typingInput("\n" + ">> ", time)
            else:
                break
        while True:
            # Age
            try:
                age = typingInput("How old are you?" + "\n" + ">> ", time)
                age = int(age)
                break
            except ValueError:
                typingPrint("Sorry I didn't recognise that age. Please type in a whole number.", time)
                continue
        # Double check responses
        correct = typingInput(f"Hello, {name}. You are a {age} year old {gender}.\nIs this correct? Y/N\n>> ", time)
        if correct.lower() in ['y', 'yes']:
            break
        elif correct.lower() in ['n', 'no']:
            continue
        else:
            typingPrint("Sorry, I didn't catch that.\n", time)
            correct = typingInput(f"You are a {age} year old {gender}. \nIs this correct? Y/N\n>> ", time)
            if correct.lower() in ['y', 'yes']:
                break
            elif correct.lower() in ['n', 'no']:
                continue
    while True:
        # Race
        race = typingInput("Please select a race from: Human, Elf, or Dwarf.\n>> ", time)
        while True:
            if race.lower() not in ("human", "elf", "dwarf"):
                race = typingInput("Sorry I didn't recognise that race. Please select 'Human', 'Elf', or 'Dwarf'.\n>> ",
                                   time)
            else:
                break
        # Job
        job = typingInput("Please select a class from: Warrior, Ranger, or Mage.\n>> ", time)
        while True:
            if job.lower() not in ("warrior", "ranger", "mage"):
                job = typingInput("Sorry I didn't recognise that class. Please select 'Warrior',"
                                  " 'Ranger', or 'Mage'.\n>> ", time)
            else:
                break
        # Final check
        correct = typingInput(f"{name}, you are a {race} {job}.\nIs this correct? Y/N\n>> ", time)
        if correct.lower() in ['y', 'yes']:
            break
        elif correct.lower() in ['n', 'no']:
            continue
        else:
            typingPrint("Sorry, I didn't catch that.\n", time)
            correct = typingInput(f"You are a {race} {job}. \nIs this correct? Y/N\n>> ", time)
            if correct.lower() in ['y', 'yes']:
                break
            elif correct.lower() in ['n', 'no']:
                continue
    return name, gender, age, race, job


# Receive action input
def parse(input_text):
    command = input_text.lower()
    object1 = ""
    # the .split() function splits the input_text string variable into a python list of individual words
    words = input_text.split()
    found_examine_words = False
    remaining_words_index = 0

    if words[0] == "examine" or words[0] == "inspect" or words[0] == "study":
        remaining_words_index = 1
        found_examine_words = True
    if words[0] == "look" and words[1] == "at":
        remaining_words_index = 2
        found_examine_words = True

    if found_examine_words:
        if len(words) > remaining_words_index:
            remaining_words = ""
            for i in range(remaining_words_index, len(words)):
                remaining_words += words[i]
                if i < len(words) - 1:
                    remaining_words += " "
            command = "examine"
            object1 = remaining_words

    found_take_words = False
    if (words[0] == "take") and len(words) > 1:
        found_take_words = True
        remaining_words_index = 1
    if (words[0] == "pick") and (words[1] == "up") and len(words) > 2:
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

    return command, object1


# Take rolled numbers and assign them to a stat
def statAllocation():
    """Rolling 4d6 to get stat value for PC"""
    rolls = []
    # roll 4d6
    for roll in range(4):
        r = randint(1, 6)
        rolls.append(r)
    # Drop the lowest number
    del rolls[rolls.index(min(rolls))]
    for i in rolls:
        print(i)
