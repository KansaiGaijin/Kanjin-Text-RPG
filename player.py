import function_list
from random import randint
from enum_list import *

class Inventory:
    def __init__(self):
        # Changed to a dictionary to store item objects as keys and their data (count, equipped, etc.) as values
        self.items = {}

    def add_item(self, item, count=1):
        if item in self.items:
            self.items[item]["Count"] += count
            print(f"Added {count} more {item.name}. Total: {self.items[item]['Count']}.")
        else:
            self.items[item] = {"Count": count, "object": item.itemType, "equipped": False}
            print(f"Added {count} {item.name} to inventory.")

    def remove_item(self, item, count=1):
        if item in self.items:
            if self.items[item]["Count"] <= count:
                print(f"Removed all {self.items[item]['Count']} {item.name} from inventory.")
                del self.items[item]
            else:
                self.items[item]["Count"] -= count
                print(f"Removed {count} {item.name} from inventory. Remaining: {self.items[item]['Count']}.")
        else:
            print(f"{item.name} not found in inventory.")

    def current_inventory(self):
        """Prints a list of items in your backpack that aren't equipped to your person."""
        print(f'In your rucksack you have:')
        if not self.items:
            print("    Your rucksack is empty.")
            return

        for item_obj, item_data in self.items.items():
            # Assuming 'equipped' is a key in item_data and Equipment.inventory holds equipped items
            # This logic needs careful alignment with how you manage equipped items.
            # For now, it checks if the item object itself is in any of the equipped slots.
            if not item_data["equipped"] and item_obj not in Equipment.inventory.values():
                count = item_data["Count"]
                print(f'{item_obj.name} x {count}\n'
                      f'    {item_obj.description}\n')

    @staticmethod
    def current_equipment():
        """Prints a list of items that you have equipped in your slots."""
        print(f'You are currently wearing:')
        equipment_found = False
        for slot, equipment in Equipment.inventory.items():
            if equipment is not None:
                equipment_found = True
                if slot == "Attunement1" or slot == "Attunement2" or slot == "Attunement3": # Assuming these are not to be printed
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
        if not equipment_found:
            print("    Nothing equipped.")

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

        # Defence
        self.ac = 0
        self.elemental_resistance = {DamageType.Fire: False, DamageType.Water: False, DamageType.Lightning: False}
        self.physical_resistance = {DamageType.Slashing: False, DamageType.Crushing: False, DamageType.Piercing: False}

        # Levels
        self.level = 1
        self.exp = 0
        self.maxEXP = 100

        # Magic (Not ready yet)
        # self.spells_known = []
        # self.spells_ready = []

        # Equipment
        # Held items
        self.inventory = Inventory()
        self.weapon = rock
        self.armor = tornRags

        # Example of adding starting items to inventory
        self.inventory.add_item(rock, 1)
        self.inventory.add_item(tornRags, 1)
        # Assuming you want to auto-equip these initially
        self.equip_item(rock, "Main Hand")
        self.equip_item(tornRags, "Chest")

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

    def drop_item(self, item_name):
        # Find the item object by name
        item_to_drop = None
        for item_obj in self.inventory.items:
            if item_obj.name.lower() == item_name.lower():
                item_to_drop = item_obj
                break

        if item_to_drop:
            self.inventory.remove_item(item_to_drop, count=1) # Remove one by default
        else:
            print(f"You don't have '{item_name}' in your inventory.")

    def loot_object(self, object_name):
        # This method assumes a specific structure for Map.scenes and lootable_items
        for scene_name, room_data in Map.scenes.items():
            if Engine.seed == scene_name:
                found_item = False
                for item_key_str, item_value_dict in room_data.get("lootable_items", {}).items():
                    # item_value_dict is like {Item_obj: count}
                    for item_obj, count in item_value_dict.items():
                        if object_name.lower() in item_obj.name.lower():
                            if count > 0:
                                self.inventory.add_item(item_obj, count)
                                room_data["lootable_items"][item_key_str][item_obj] = 0 # Set count to 0 in room
                                found_item = True
                                break
                    if found_item:
                        break
                if not found_item:
                    print("You don't see one of those to loot.")
                return # Exit after checking the current room

    def add_inventory(self, object_name):
        # This method assumes a specific structure for Map.scenes and available_items
        for scene_name, room_data in Map.scenes.items():
            if Engine.seed == scene_name:
                found_item = False
                for item_key_str, item_value_dict in room_data.get("available_items", {}).items():
                    # item_value_dict is like {Item_obj: count}
                    for item_obj, count_available in item_value_dict.items():
                        if object_name.lower() in item_obj.name.lower():
                            if count_available == 0:
                                print(f"There are no {item_obj.name} left here.")
                                found_item = True
                                break

                            response = input(f'There are {count_available} {item_obj.name} available.\n'
                                             f'How many will you take? (enter "all" or a number)\n>> ').lower()

                            if response == "0" or response == "none":
                                print("You decide not to take any.")
                                found_item = True
                                break
                            elif response == "all":
                                self.inventory.add_item(item_obj, count_available)
                                room_data["available_items"][item_key_str][item_obj] = 0
                                found_item = True
                                break
                            elif response.isdigit():
                                num_to_take = int(response)
                                if num_to_take <= count_available:
                                    self.inventory.add_item(item_obj, num_to_take)
                                    room_data["available_items"][item_key_str][item_obj] -= num_to_take
                                    found_item = True
                                    break
                                else:
                                    print("You can't take more than exist.")
                                    found_item = True
                                    break
                            else:
                                print("Invalid input. Please enter 'all' or a number.")
                                found_item = True
                                break
                    if found_item:
                        break
                if not found_item:
                    print("You don't see any lying around.")
                return  # Exit after checking the current room

    def equip_item(self, item_obj, slot):
        """Equips an item to a specific slot."""
        if item_obj in self.inventory.items and self.inventory.items[item_obj]["Count"] > 0:
            # Unequip existing item in that slot if any
            if Equipment.inventory[slot] is not None:
                unequipped_item = Equipment.inventory[slot]
                print(f"Unequipping {unequipped_item.name} from {slot}.")
                self.inventory.items[unequipped_item]["equipped"] = False  # Mark as unequipped in inventory

            Equipment.inventory[slot] = item_obj
            self.inventory.items[item_obj]["equipped"] = True
            print(f"Equipped {item_obj.name} to {slot}.")
        else:
            print(f"You don't have {item_obj.name} to equip.")

    def unequip_item(self, slot):
        """Unequips an item from a specific slot."""
        if Equipment.inventory[slot] is not None:
            unequipped_item = Equipment.inventory[slot]
            self.inventory.items[unequipped_item]["equipped"] = False
            Equipment.inventory[slot] = None
            print(f"Unequipped {unequipped_item.name} from {slot}.")
        else:
            print(f"Nothing is equipped in {slot}.")

    def new_char(self):
        """Outputs final stats, armour, and inventory"""
        self.allocation()
        self.set_stats_race()
        self.set_stats_job()
        self.getModifier()
        self.current_stats()
        print(' ')
        Inventory.current_equipment()  # Call the static method of Inventory
        print(' ')
        self.inventory.current_inventory()  # Call the instance method of Player's inventory
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
                    # This rolling logic (if r < 6: r = randint(1, 6)) seems to aim for higher rolls.
                    # Standard D&D 4d6 drop lowest usually means you just roll 4 and drop the lowest.
                    # I'll keep your original logic but note it's non-standard.
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
            current_attributes = list(attributes)  # Make a copy to modify
            current_stats_to_assign = list(stats)  # Make a copy

            while len(current_stats_to_assign) != 0:
                input_text = input(">> ").title()
                words = input_text.split()
                if len(words) == 2:
                    try:
                        chosen_stat_str = words[0]
                        chosen_attribute = words[1]

                        if chosen_stat_str in current_stats_to_assign and chosen_attribute in current_attributes:
                            self.stats[chosen_attribute] += int(chosen_stat_str)
                            current_stats_to_assign.remove(chosen_stat_str)
                            current_attributes.remove(chosen_attribute)
                            if len(current_stats_to_assign) == 1:
                                self.stats[current_attributes[0]] += int(current_stats_to_assign[0])
                                print("")
                                break
                            print(f"The remaining stats are:\n {', '.join(current_stats_to_assign)}\n\n"
                                  f"The remaining attributes are:\n {', '.join(current_attributes)}")
                        else:
                            print(
                                "Error. Either the number or attribute was not available/recognised. Please try again with 'Number' + 'Attribute'.")
                    except ValueError:
                        print("Error. Invalid number format. Please try again with 'Number' + 'Attribute'.")
                    except KeyError:
                        print("Error. Attribute not recognized. Please try again with 'Number' + 'Attribute'.")
                else:
                    print("Error. Input was not recognised. Please try again with 'Number' + 'Attribute'.")

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
                # Reset stats for re-allocation
                self.stats = {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0,
                              "Charisma": 0}
                continue
            elif select == 'y':
                break
            else:
                print("Error. Input was not recognised. Please select 'Y' or 'N'.")
                # Loop back to ask again or handle as desired

class Item:
    """The base class for all items"""

    def __init__(self, name, description, value, magical, itemType, attunement):
        self.name = name
        self.description = description
        self.value = value
        self.magical = magical
        self.itemType = itemType
        self.attunement = attunement

    def __repr__(self):
        return f"{self.name}\n=====\n{self.description}\nValue: {self.value}\n"


class Money(Item):
    """The currency item used in the world of Kanjin"""

    def __init__(self, name, amt, magical, ItemType):
        self.name = name
        self.amt = amt
        self.magical = magical
        self.itemType = ItemType
        super().__init__(name=self.name,
                         description=f"A small round coin made of {self.name.lower()} "
                                     f"with the imperial city logo stamped on the face.",
                         value=self.amt,
                         magical=self.magical,
                         ItemType=ItemType.Money,
                         attunement=False)


class Weapon(Item):
    """The base class for all weapons"""

    def __init__(self, name, description, value, slot, damage1H, damage2H, versatiledmg,
                 dmgType, dmgMod, versatile, thrown, ItemType, magical, attunement):
        self.slot = slot
        self.damage1H = damage1H
        self.damage2H = damage2H
        self.versatiledmg = versatiledmg
        self.dmgType = dmgType
        self.dmgMod = dmgMod
        self.versatile = versatile
        self.thrown = thrown
        self.itemType = ItemType
        super().__init__(name, description, value, magical, ItemType, attunement)

    def __str__(self):
        if self.damage2H is None and self.damage1H is not None:
            return f"{self.name}\n=====" \
                   f"\n{self.description}" \
                   f"\nValue: {self.value}" \
                   f"\nDamage: One Handed - {self.damage1H}" \
                   f"\nDamage Type: {self.dmgType.name.title()}" \
                   f"\nMagical: {self.magical}" \
                   f"\nAttunement: {'Required' if self.attunement else 'Not Required'}"
        elif self.damage1H is None and self.damage2H is not None:
            return f"{self.name}\n=====" \
                   f"\n{self.description}" \
                   f"\nValue: {self.value}" \
                   f"\nDamage: Two Handed - {self.damage2H}" \
                   f"\nDamage Type: {self.dmgType.name.title()}" \
                   f"\nMagical: {self.magical}" \
                   f"\nAttunement: {'Required' if self.attunement else 'Not Required'}"
        elif self.versatile:
            return f"{self.name}\n=====" \
                   f"\n{self.description}" \
                   f"\nValue: {self.value}" \
                   f"\nDamage: Versatile - {self.versatiledmg}" \
                   f"\nDamage Type: {self.dmgType.name.title()}" \
                   f"\nMagical: {self.magical}" \
                   f"\nAttunement: {'Required' if self.attunement else 'Not Required'}"
        else:
            return f"{self.name}\n=====" \
                   f"\n{self.description}" \
                   f"\nValue: {self.value}" \
                   f"\nMagical: {self.magical}" \
                   f"\nAttunement: {'Required' if self.attunement else 'Not Required'}"


class Armor(Item):
    """The base class for all armor"""

    def __init__(self, name, description, value, grade, ac, disadvantage, dmgRes, ItemType, magical, attunement):
        self.grade = grade
        self.ac = ac
        self.stealthDis = disadvantage
        self.dmgRes = dmgRes
        self.itemType = ItemType
        super().__init__(name, description, value, magical, ItemType, attunement)

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
GP1 = Money("Gold", 1, False, ItemType.Money)
SP1 = Money("Silver", 1, False, ItemType.Money)
CP1 = Money("Copper", 1, False, ItemType.Money)

# starting equip
rock = Weapon(
    name="Rock",
    description="A fist-sized rock, suitable for bludgeoning.",
    value=None,
    slot="Main Hand",
    damage1H='1d6',
    damage2H=None,
    versatiledmg=None,
    dmgType=DamageType.Crushing,
    dmgMod=DamageMod.Strength,
    versatile=False,
    thrown=True,
    magical=False,
    ItemType=ItemType.Weapon,
    attunement=True
)

dagger = Weapon(
    name="Dagger",
    description="Pointy stabby-stab",
    value=None,
    slot="Main Hand",
    damage1H=None,
    damage2H=None,
    versatiledmg='1d6',
    dmgType=DamageType.Slashing,
    dmgMod=DamageMod.Dexterity,
    versatile=True,
    thrown=True,
    magical=False,
    ItemType=ItemType.Weapon,
    attunement=True
)

polearm = Weapon(
    name="Polearm",
    description="Long Pointy stabby-stab",
    value=None,
    slot="Two Handed",
    damage1H=None,
    damage2H="2d6",
    versatiledmg=None,
    dmgType=DamageType.Piercing,
    dmgMod=DamageMod.Strength,
    versatile=False,
    thrown=True,
    magical=False,
    ItemType=ItemType.Weapon,
    attunement=True
)

tornRags = Armor(
    name="Torn Rags",
    description="A ripped and worn-out outfit.",
    value=None,
    grade="Light",
    ac=0,
    disadvantage=True,
    dmgRes="None",
    magical=False,
    ItemType=ItemType.Armor,
    attunement=True
)
paper = Item(
    name="Paper",
    description="A blank piece of paper",
    value=None,
    magical=False,
    ItemType=ItemType.Item,
    attunement=True
)

Inventory = {
        rock: {"Count": 1,
               "object": Weapon,
               },
        dagger: {"Count": 1,
                 "object": Weapon,
                 },
        polearm: {"Count": 1,
                  "object": Weapon
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
    "Other": paper,
    "Attunement": 0
}

