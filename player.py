from enum import Enum, auto
from random import randint


class Player:
    """Character Creation"""

    # Default Character
    def __init__(self, name, gender, age, race, job):
        # Identity
        self.name = name
        self.gender = gender
        self.age = age
        self.race = race
        self.job = job
        # Health (move off Player, keep on Job)
        # self.hitDie = self.job.hd
        # self.currentHP = 100
        # self.maxHP = 100
        # Levels
        self.level = 1
        self.exp = 0
        self.maxEXP = 100
        # Magic (Not ready yet)
        # self.spells_known = []
        # self.spells_ready = []
        # Equipment
        self.weapon = rock
        self.armor = tornRags
        # Defence
        self.ac = 0
        self.elemental_resistance = {DamageType.Fire: False, DamageType.Water: False, DamageType.Lightning: False}
        self.physical_resistance = {DamageType.Slashing: False, DamageType.Crushing: False, DamageType.Piercing: False}
        # Ability Scores
        self.stats = {"Strength": 0,
                      "Dexterity": 0,
                      "Constitution": 0,
                      "Intelligence": 0,
                      "Wisdom": 0,
                      "Charisma": 0}
        # Ability Modifiers
        self.mods = {"Strength": 0,
                     "Dexterity": 0,
                     "Constitution": 0,
                     "Intelligence": 0,
                     "Wisdom": 0,
                     "Charisma": 0}
        # Held items
        self.inventory = {rock: {"Count": 1,
                                 "object": Weapon,
                                 "equipped": True
                                 },
                          paper: {"Count": 1,
                                  "object": Weapon,
                                  "equipped": False
                                  },
                          tornRags: {"Count": 1,
                                     "object": Armor,
                                     "equipped": True
                                     },
                          GP1: {"Count": 10,
                                "object": Money,
                                "equipped": False
                                },
                          }

    def getModifier(self):
        """Floor calculation to work out skill check modifiers"""
        self.mods["Strength"] = -5 + self.stats["Strength"] // 2
        self.mods["Dexterity"] = -5 + self.stats["Dexterity"] // 2
        self.mods["Constitution"] = -5 + self.stats["Constitution"] // 2
        self.mods["Intelligence"] = -5 + self.stats["Intelligence"] // 2
        self.mods["Wisdom"] = -5 + self.stats["Wisdom"] // 2
        self.mods["Charisma"] = -5 + self.stats["Charisma"] // 2

    def set_stats_race(self):
        if self.race.lower() == "human":
            print("As a Human, two different ability scores of your choice increase by 1.")
            selection1 = input("Choose the first ability score to increase by 1.\n"
                               "1) Strength\n"
                               "2) Dexterity\n"
                               "3) Constitution\n"
                               "4) Intelligence\n"
                               "5) Wisdom\n"
                               "6) Charisma\n\n >> ").lower()
            while True:
                if selection1 in ("1", "strength"):
                    self.stats["Strength"] += 1
                    break
                elif selection1 in ("2", "dexterity"):
                    self.stats["Dexterity"] += 1
                    break
                elif selection1 in ("3", "constitution"):
                    self.stats["Constitution"] += 1
                    break
                elif selection1 in ("4", "intelligence"):
                    self.stats["Intelligence"] += 1
                    break
                elif selection1 in ("5", "wisdom"):
                    self.stats["Wisdom"] += 1
                    break
                elif selection1 in ("6", "charisma"):
                    self.stats["Charisma"] += 1
                    break
                else:
                    selection1 = input("Sorry, I didn't recognise that. Please select from the following:\n"
                                       "1) Strength\n"
                                       "2) Dexterity\n"
                                       "3) Constitution\n"
                                       "4) Intelligence\n"
                                       "5) Wisdom\n"
                                       "6) Charisma\n >> ").lower()
                    continue

            selection2 = input("Choose the second ability score to increase by 1.\n"
                               "1) Strength\n"
                               "2) Dexterity\n"
                               "3) Constitution\n"
                               "4) Intelligence\n"
                               "5) Wisdom\n"
                               "6) Charisma\n\n >> ").lower()
            while True:
                if selection2 in ("1", "strength"):
                    self.stats["Strength"] += 1
                    break
                elif selection2 in ("2", "dexterity"):
                    self.stats["Dexterity"] += 1
                    break
                elif selection2 in ("3", "constitution"):
                    self.stats["Constitution"] += 1
                    break
                elif selection2 in ("4", "intelligence"):
                    self.stats["Intelligence"] += 1
                    break
                elif selection2 in ("5", "wisdom"):
                    self.stats["Wisdom"] += 1
                    break
                elif selection2 in ("6", "charisma"):
                    self.stats["Charisma"] += 1
                    break
                else:
                    selection2 = input("Sorry, I didn't recognise that. Please select from the following:\n"
                                       "1) Strength\n"
                                       "2) Dexterity\n"
                                       "3) Constitution\n"
                                       "4) Intelligence\n"
                                       "5) Wisdom\n"
                                       "6) Charisma\n >> ").lower()
                    continue

        elif self.race.lower() == "elf":
            self.stats["Dexterity"] += 2

        elif self.race.lower() == "dwarf":
            self.stats["Constitution"] += 2

    def set_stats_job(self):
        if self.job.lower() == "warrior":
            self.hitDie = randint(1, 12)
            self.maxHP = (12 + self.mods["Constitution"])
            self.currentHP = (12 + self.mods["Constitution"])

        elif self.job.lower() == "cleric":
            self.hitDie = randint(1, 10)
            self.maxHP = (10 + self.mods["Constitution"])
            self.currentHP = (10 + self.mods["Constitution"])

        elif self.job.lower() == "mage":
            self.hitDie = randint(1, 8)
            self.maxHP = (8 + self.mods["Constitution"])
            self.currentHP = (8 + self.mods["Constitution"])

    def current_stats(self):
        """Prints a display of the user's current statistics."""
        print("Your current stats are:")
        print(f'Hit Points: {self.currentHP}/{self.maxHP}')
        print(f'Strength: {self.stats["Strength"]}')
        print(f'Dexterity: {self.stats["Dexterity"]}')
        print(f'Constitution: {self.stats["Constitution"]}')
        print(f'Intelligence: {self.stats["Intelligence"]}')
        print(f'Wisdom: {self.stats["Wisdom"]}')
        print(f'Charisma: {self.stats["Charisma"]}')

    def current_equip(self):
        """Prints a list of items currently equipped."""
        print(f"You have equipped:\n {self.armor.name}\n"
              f"    {self.armor.description}"
              f"\n{self.weapon.name}\n"
              f"    {self.weapon.description}")

    def drop_item(self, object1):
        x = None
        for list_key, list_value in self.inventory.items():  # string, dictionary
            if object1 in list_key.name.lower():  # if user input is in the inventory list
                x = self.inventory.copy()
                del x[list_key]
                print("Did I drop it?")
        return x

    # Add the inventory commands to parser // take off Player

    def update_inventory(self, x):
        self.inventory = x

    def loot_object(self, object1):
        for scene, room in Map.scenes.items():  # iterate map scenes
            if Engine.seed == scene:  # set new Engine seed in each room.enter()
                for list_key, list_value in room.lootable_items.items():  # string, dictionary
                    for var, count in list_value.items():  # variable/object, integer
                        if object1 in list_key:  # if user input is in the lootable items

                            if var in self.inventory:  # if object is in inventory
                                self.inventory[var]["Count"] += count  # increase item count
                                print(f'{var.name} x {count} has been added to your existing stack.')

                            elif var not in self.inventory[var]:  # if variable not in inventory
                                self.inventory[var] = {"Count": count,  # add it in
                                                       "object": var.type,
                                                       "equipped": False}
                                print(f'{var.name} x {count} has been added to your rucksack.')

                        room.lootable_items[object1][var] = 0  # set item to 0
                        break
                    else:
                        print("You don't see one of those to loot.")
                        break

    def add_inventory(self, object1):
        for scene, room in Map.scenes.items():  # iterate map scenes
            if Engine.seed == scene:  # set new Engine seed in each room.enter()
                for list_key, list_value in room.available_items.items():  # string, dictionary
                    for var, count in list_value.items():  # variable/object, integer
                        if object1 in list_key:  # if user input is in the available items

                            response = input(f'There are {room.available_items[object1][var]}.\n'
                                             f'How many will you take?\n>> ').lower()
                            if response in ("0", "none"):
                                break
                            elif response == "all":
                                if var in self.inventory:
                                    self.inventory[var]["Count"] += count  # increase item count
                                    print(f'{var.name} x {count} has been added to your existing stack.')
                                    room.available_items[object1][var] = 0

                                elif var not in self.inventory:  # if objects not in inventory
                                    self.inventory[var] = {"Count": count,  # add it in
                                                           "object": var.type,
                                                           "equipped": False}
                                    print(f'{var.name} x {count} has been added to your rucksack.')
                                    room.available_items[object1][var] = 0

                            elif int(response) <= count:
                                if var in self.inventory:
                                    self.inventory[var]["Count"] += int(response)  # increase item count
                                    print(f'{var.name} x {response} has been added to your existing stack.')
                                    room.available_items[object1][var] = \
                                        room.available_items[object1][var] - int(response)

                                elif var not in self.inventory:  # if objects not in inventory
                                    self.inventory[var] = {"Count": response,  # add it in
                                                           "object": var.type,
                                                           "equipped": False}
                                    print(f'{var.name} x {response} has been added to your rucksack.')
                                    room.available_items[object1][var] = \
                                        room.available_items[object1][var] - int(response)

                            else:
                                print("You can't take more than exist.")

                        break
                    else:
                        print("You don't see any lying around..")
                        break

    def new_char(self):
        """Outputs final stats, armour, and inventory"""
        self.allocation()
        self.set_stats_race()
        self.set_stats_job()
        self.getModifier()
        self.current_stats()
        print(' ')
        functions.current_equipment()
        print(' ')
        functions.current_inventory()
        print(' ')

    def health_check(self):
        """Print out current/max HP"""
        print(f'You have {self.currentHP}/{self.maxHP} HP.')

    def take_damage(self, DMGtype, size):
        """Define the damage type and dice size"""
        damage = randint(1, size)
        if DMGtype in self.elemental_resistance or DMGtype in self.physical_resistance:
            damage //= 2
        self.currentHP -= damage
        return damage

    def allocation(self):
        while True:
            rolls = []
            stats = []
            attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
            while len(stats) != 6:
                # roll 4d6
                for roll in range(4):
                    r = randint(1, 6)
                    if r < 6:
                        r = randint(1, 6)
                    rolls.append(r)
                # Drop the lowest number and then add to single value
                del rolls[rolls.index(min(rolls))]
                val = sum(rolls)
                stats.append(str(val))
                rolls = []

            print(f"Please assign a stat to a selected attribute by entering the number then the attribute.\n"
                  f"For example, '10 strength' will assign 10 to your strength, if you have a 10 available.\n\n"
                  f"Please select a stat and an attribute.\n\n"
                  f"Your rolled stats are:\n {', '.join(stats)}\n\n"
                  f"Your attributes are:\n {', '.join(attributes)}\n")

            # Allocate
            while len(stats) != 0:
                input_text = input(">> ").title()
                words = input_text.split()
                if len(words) < 2:
                    if words[0] in stats and words[1] in attributes:
                        self.stats[words[1]] += int(words[0])
                        stats.remove(words[0])
                        attributes.remove(words[1])
                        if len(stats) == 1:
                            self.stats[attributes[0]] += int(stats[0])
                            print("")
                            break
                        print(f"The remaining stats are:\n {', '.join(stats)}\n\n"
                              f"The remaining attributes are:\n {', '.join(attributes)}")
                    else:
                        print("Error. Input was not recognised. Please try again with 'Number' + 'Attribute'.")
                        continue
                else:
                    print("Error. Input was not recognised. Please try again with 'Number' + 'Attribute'.")
                    continue

            print(f"Your current stats are:\n"
                  f'Strength: {self.stats["Strength"]}\n'
                  f'Dexterity: {self.stats["Dexterity"]}\n'
                  f'Constitution: {self.stats["Constitution"]}\n'
                  f'Intelligence: {self.stats["Intelligence"]}\n'
                  f'Wisdom: {self.stats["Wisdom"]}\n'
                  f'Charisma: {self.stats["Charisma"]}\n')

            select = input("Are you happy with this selection? Y/N?\n"
                           "WARNING: If you select 'N', your dice will be randomly rolled again. Proceed?\n"
                           " >> ").lower()
            if select == "n":
                continue
            if select == 'y':
                break

            elif select not in ("y", "n"):
                print("Error. Input was not recognised. Please select 'Y' or 'N'.")
                select = input("Are you happy with this selection? Y/N?\n"
                               "WARNING: If you select 'N', your dice will be randomly rolled again. Proceed?\n"
                               " >> ").lower()
                if select == "y":
                    break
                else:
                    continue


class DamageType(Enum):
    Slashing = auto()
    Crushing = auto()
    Piercing = auto()
    Fire = auto()
    Water = auto()
    Lightning = auto()


class DamageMod(Enum):
    Strength = auto()
    Dexterity = auto()
    Constitution = auto()
    Intelligence = auto()
    Wisdom = auto()
    Charisma = auto()


class ItemType(Enum):
    Armor = auto()
    Weapon = auto()
    Money = auto()
    Item = auto()


class Slots(Enum):
    MainHand = auto()
    OffHand = auto()
    TwoHanded = auto()
    Helm = auto()
    Chest = auto()
    Wrists = auto()
    Feet = auto()
    Neck = auto()
    Cloak = auto()
    LeftRing = auto()
    RightRing = auto()
    Attunement = auto()


class Item:
    """The base class for all items"""

    def __init__(self, name, description, value, magical):
        self.name = name
        self.description = description
        self.value = value
        self.magical = magical
        self.type = ItemType.Item

    def __repr__(self):
        return f"{self.name}\n=====\n{self.description}\nValue: {self.value}\n"


class Money(Item):
    """The currency item used in the world of Kanjin"""

    def __init__(self, name, amt, magical):
        self.name = name
        self.amt = amt
        self.magical = magical
        self.type = ItemType.Money
        super().__init__(name=self.name,
                         description=f"A small round coin made of {self.name.lower()} "
                                     f"with the imperial city logo stamped on the face.",
                         value=self.amt,
                         magical=self.magical)


class Weapon(Item):
    """The base class for all weapons"""

    def __init__(self, name, description, value, slot, damage1H, damage2H,
                 dmgType, dmgMod, versatile, thrown, magical):
        self.slot = slot
        self.damage1H = damage1H
        self.damage2H = damage2H
        self.dmgType = dmgType
        self.dmgMod = dmgMod
        self.versatile = versatile
        self.thrown = thrown
        self.itemType = ItemType.Weapon
        self.attunement = False
        super().__init__(name, description, value, magical)

    def __repr__(self):
        return f"{self.name}\n=====" \
               f"\n{self.description}" \
               f"\nValue: {self.value}" \
               f"\nDamage: One Handed - {self.damage1H}" \
               f"\nDamage: Two Handed - {self.damage2H}" \
               f"\nDamage Type: {self.dmgType.name.title()}" \
               f"\nMagical: {self.magical}"


class Armor(Item):
    """The base class for all armor"""

    def __init__(self, name, description, value, grade, ac, disadvantage, dmgRes, magical):
        self.grade = grade
        self.ac = ac
        self.stealthDis = disadvantage
        self.dmgRes = dmgRes
        self.itemType = ItemType.Armor
        super().__init__(name, description, value, magical)

    def __repr__(self):
        if self.stealthDis:
            return f"{self.name}\n" \
                   f"=====\n" \
                   f"{self.description}\n" \
                   f"Value: {self.value}\n" \
                   f"AC: {self.ac}\n" \
                   f"Magical: {self.magical}"
        elif not self.stealthDis:
            return f"{self.name}\n=====" \
                   f"\n{self.description}\n" \
                   f"Value: {self.value}\n" \
                   f"AC: {self.ac}\n" \
                   f"Disadvantage on Stealth checks: {self.stealthDis}\n" \
                   f"Magical: {self.magical}\n"


# Different types of coins
GP1 = Money("Gold", 1, False)
SP1 = Money("Silver", 1, False)
CP1 = Money("Copper", 1, False)

# starting equip
rock = Weapon(
    name="Rock",
    description="A fist-sized rock, suitable for bludgeoning.",
    value=None,
    slot=Slots.MainHand,
    damage1H='1d6',
    damage2H=None,
    dmgType=DamageType.Crushing,
    dmgMod=DamageMod.Strength,
    versatile=False,
    thrown=True,
    magical=False
)

dagger = Weapon(
    name="Dagger",
    description="Pointy stabby-stab",
    value=None,
    slot=Slots.MainHand,
    damage1H='1d6',
    damage2H=None,
    dmgType=DamageType.Slashing,
    dmgMod=DamageMod.Dexterity,
    versatile=False,
    thrown=True,
    magical=False
)

tornRags = Armor(
    name="Torn Rags",
    description="A ripped and worn-out outfit.",
    value=None,
    grade="Light",
    ac=0,
    disadvantage=True,
    dmgRes="None",
    magical=False
)
paper = Item(
    name="Paper",
    description="A blank piece of paper",
    value=None,
    magical=False
)

Inventory = {
        rock: {"Count": 1,
               "object": Weapon,
               },
        dagger: {"Count": 1,
                 "object": Weapon,
                 },
        paper: {"Count": 1,
                "object": Item
                },
        tornRags: {"Count": 1,
                   "object": Armor
                   },
        GP1: {"Count": 10,
              "object": Money
              },
}

Equipment = {
    "Main Hand": rock,
    "Off Hand": None,
    "Two Handed": None,
    "Helm": None,
    "Chest": tornRags,
    "Wrists": None,
    "Feet": None,
    "Neck": None,
    "Cloak": None,
    "Left Ring": None,
    "Right Ring": None,
    "Attunement": None
}

