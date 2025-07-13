from random import randint
from enum_list import DamageType, DamageMod, ItemType, Slots # Import specific enums

# Define Item classes here, as they are fundamental building blocks
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
                         itemType=ItemType.Money,
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
                   f"\n{self.description}\n" \
                   f"Value: {self.value}\n" \
                   f"Magical: {self.magical}\n" \
                   f"Attunement: {'Required' if self.attunement else 'Not Required'}"

class Armor(Item):
    """The base class for all armor"""
    def __init__(self, name, description, value, slot, grade, ac, disadvantage, dmgRes, ItemType, magical, attunement):
        self.slot = slot
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
        return None


class Inventory:
    def __init__(self):
        # Dictionary to store item objects as keys and their data (count) as values
        self.items = {}
        # Dictionary to store equipped items by slot
        self.equipped_items = {
            Slots.MainHand: None,
            Slots.OffHand: None,
            Slots.TwoHanded: None,
            Slots.Helm: None,
            Slots.Chest: None,
            Slots.Wrists: None,
            Slots.Feet: None,
            Slots.Neck: None,
            Slots.Cloak: None,
            Slots.LeftRing: None,
            Slots.RightRing: None,
            Slots.Other: None, # For miscellaneous equipped items
            Slots.Attunement: 0 # Counter for attuned items
        }

    def _get_slot_display_name(self, slot_val):
        """Helper to get a user-friendly string name for a slot, handling both Enum and string inputs."""
        if isinstance(slot_val, Slots):
            return slot_val.name.replace('TwoHanded', 'Two Handed').replace('MainHand',
                                        'Main Hand').replace('OffHand',
                                        'Off Hand').replace('LeftRing', 'Left Ring').replace(
                                         'RightRing', 'Right Ring')
        elif isinstance(slot_val, str):
            # If it's already a string, assume it's the name and format it
            return (slot_val.replace('TwoHanded', 'Two Handed').replace('MainHand', 'Main Hand')
                            .replace('OffHand','Off Hand').replace('LeftRing', 'Left Ring')
                            .replace('RightRing', 'Right Ring'))
        return str(slot_val)  # Fallback for unexpected types

    def add_item(self, item, count=1):
        """Adds an item to the inventory."""
        if item in self.items:
            self.items[item]["Count"] += count
            print(f"Added {count} more {item.name}. Total: {self.items[item]['Count']}.")
        else:
            self.items[item] = {"Count": count, "object": item.itemType}
            print(f"Added {count} {item.name} to inventory.")

    def remove_item(self, item, count=1):
        """Removes an item from the inventory."""
        if item in self.items:
            if self.items[item]["Count"] <= count:
                print(f"Removed all {self.items[item]['Count']} {item.name} from inventory.")
                del self.items[item]
                # If the item was equipped, unequip it
                for slot, equipped_item in self.equipped_items.items():
                    if equipped_item == item:
                        self.unequip_item(slot)
            else:
                self.items[item]["Count"] -= count
                print(f"Removed {count} {item.name} from inventory. Remaining: {self.items[item]['Count']}.")
        else:
            print(f"{item.name} not found in inventory.")

    def current_inventory(self):
        """Prints a list of items in your backpack that aren't equipped to your person."""
        print(f'In your rucksack you have:')
        found_un_equipped = False
        for item_obj, item_data in self.items.items():
            # Check if the item is in the backpack AND not currently equipped in any slot
            if item_obj not in self.equipped_items.values():
                found_un_equipped = True
                count = item_data["Count"]
                print(f'{item_obj.name} x {count}\n'
                      f'    {item_obj.description}\n')
        if not found_un_equipped:
            print("    Your rucksack is empty.")

    def current_equipment(self):
        """Prints a list of items that you have equipped in your slots."""
        print(f'You are currently wearing:')
        equipment_found = False
        for slot, equipment in self.equipped_items.items():
            if equipment is not None and slot != Slots.Attunement: # Don't print the attunement counter
                equipment_found = True
                slot_name = slot.name.replace("TwoHanded", "Two Handed").replace("MainHand", "Main Hand").replace("OffHand", "Off Hand").replace("LeftRing", "Left Ring").replace("RightRing", "Right Ring")
                if equipment.itemType == ItemType.Weapon:
                    if equipment.versatile:
                        print(f'{slot_name}: {equipment.name} - {equipment.versatiledmg}\n'
                              f'    {equipment.description}\n')
                    elif equipment.damage1H is not None:
                        print(f'{slot_name}: {equipment.name} - {equipment.damage1H}\n'
                              f'    {equipment.description}\n')
                    elif equipment.damage2H is not None:
                        print(f'{slot_name}: {equipment.name} - {equipment.damage2H}\n'
                              f'    {equipment.description}\n')
                elif equipment.itemType == ItemType.Armor:
                    print(f'{slot_name}: {equipment.name} - AC {equipment.ac}\n'
                          f'    {equipment.description}\n')
                elif equipment.itemType == ItemType.Item:
                    print(f'{slot_name}: {equipment.name}\n'
                          f'    {equipment.description}\n')
        if not equipment_found:
            print("    Nothing equipped.")
        print(f"Attunement slots used: {self.equipped_items[Slots.Attunement]}/3")


    def equip_item(self, item_obj, slot: Slots):
        """Equips an item to a specific slot."""
        if item_obj not in self.items or self.items[item_obj]["Count"] == 0:
            print(f"You don't have {item_obj.name} to equip.")
            return

        # Check attunement limits before equipping (moved up for early exit)
        if item_obj.attunement and self.equipped_items[Slots.Attunement] >= 3:
            print(f"You cannot equip {item_obj.name}. You have reached your attunement limit (3/3).")
            return

        # Handle unequipping existing item in the target slot first
        if self.equipped_items[slot] is not None:
            self.unequip_item(slot)

        # Now, handle equipping based on item type and specific properties
        if item_obj.itemType == ItemType.Weapon:
            if item_obj.slot == Slots.TwoHanded:
                # If equipping a two-handed weapon, unequip anything in main/off-hand
                if self.equipped_items[Slots.MainHand] is not None:
                    self.unequip_item(Slots.MainHand)
                if self.equipped_items[Slots.OffHand] is not None:
                    self.unequip_item(Slots.OffHand)
                self.equipped_items[Slots.TwoHanded] = item_obj
                print(f"Equipped {item_obj.name} to {self._get_slot_display_name(Slots.TwoHanded)}.")
            elif item_obj.versatile:
                # If equipping a versatile weapon, it goes in MainHand, and potentially affects OffHand
                if self.equipped_items[Slots.TwoHanded] is not None:
                    self.unequip_item(Slots.TwoHanded) # Unequip two-handed if present
                self.equipped_items[Slots.MainHand] = item_obj
                # A versatile weapon can be used two-handed, implying it might occupy the off-hand conceptually
                # For simplicity, we'll just equip it to MainHand here. If you want it to occupy off-hand,
                # you'd need more complex logic for 1H vs 2H use.
                print(f"Equipped {item_obj.name} to {self._get_slot_display_name(Slots.MainHand)}.")
            else: # Standard one-handed weapon (or other weapon types not specifically handled above)
                self.equipped_items[slot] = item_obj # Equip to the specified slot (MainHand or OffHand)
                print(f"Equipped {item_obj.name} to {self._get_slot_display_name(slot)}.")
        elif item_obj.itemType == ItemType.Armor:
            # For armor, ensure the target slot is appropriate for armor (e.g., Chest, Helm)
            # The Armor class now has a 'slot' attribute, so we can use that for validation/assignment
            if item_obj.slot == slot: # Ensure the item's intended slot matches the target slot
                self.equipped_items[slot] = item_obj
                print(f"Equipped {item_obj.name} to {self._get_slot_display_name(slot)}.")
            else:
                # Corrected this line to use _get_slot_display_name for both slot and item_obj.slot
                print(f"Cannot equip {item_obj.name} to {self._get_slot_display_name(slot)}. It belongs in the {self._get_slot_display_name(item_obj.slot)} slot.")
                return # Exit if slot mismatch
        elif item_obj.itemType == ItemType.Item:
            # For general items (rings, cloaks, etc.), equip to the specified slot
            self.equipped_items[slot] = item_obj
            print(f"Equipped {item_obj.name} to {self._get_slot_display_name(slot)}.")
        else:
            print(f"Cannot equip {item_obj.name}. Unknown item type or invalid slot for this item.")
            return # Exit if item type is not recognized for equipping

        self.update_attunement() # Update attunement after successful equip


    def unequip_item(self, slot: Slots):
        """Unequips an item from a specific slot."""
        if self.equipped_items[slot] is not None:
            unequipped_item = self.equipped_items[slot]
            self.equipped_items[slot] = None
            print(f"Unequipped {unequipped_item.name} from {self._get_slot_display_name(slot)}.") # Use helper function
            self.update_attunement()
        else:
            print(f"Nothing is equipped in {self._get_slot_display_name(slot)}.") # Use helper function

    def update_attunement(self):
        """Recalculates the number of attuned items."""
        attune_count = 0
        for slot, item in self.equipped_items.items():
            if slot != Slots.Attunement and item is not None and item.attunement:
                attune_count += 1
        self.equipped_items[Slots.Attunement] = attune_count


# --- Item Instances (Moved here for clarity, but still defined once) ---
# Different types of coins
GP1 = Money("Gold", 1, False, ItemType.Money)
SP1 = Money("Silver", 1, False, ItemType.Money)
CP1 = Money("Copper", 1, False, ItemType.Money)

# starting equip
rock = Weapon(
    name="Rock",
    description="A fist-sized rock, suitable for bludgeoning.",
    value=None,
    slot=Slots.MainHand,
    damage1H='1d6',
    damage2H=None,
    versatiledmg=None,
    dmgType=DamageType.Bludgeoning,
    dmgMod=DamageMod.Strength,
    versatile=False,
    thrown=True,
    magical=False,
    ItemType=ItemType.Weapon,
    attunement=False # Rocks typically aren't attuned
)

dagger = Weapon(
    name="Dagger",
    description="Pointy stabby-stab",
    value=None,
    slot=Slots.MainHand, # Can be main hand or off hand
    damage1H='1d4', # Daggers are usually 1d4
    damage2H=None,
    versatiledmg=None, # Daggers are not versatile in the D&D sense (they are light, finesse)
    dmgType=DamageType.Piercing, # Changed to piercing
    dmgMod=DamageMod.Dexterity,
    versatile=False, # Changed to False, as D&D versatile means 1H or 2H damage
    thrown=True,
    magical=False,
    ItemType=ItemType.Weapon,
    attunement=False
)

polearm = Weapon(
    name="Polearm",
    description="Long Pointy stabby-stab",
    value=None,
    slot=Slots.TwoHanded,
    damage1H=None,
    damage2H="1d10", # Polearms are typically 1d10
    versatiledmg=None,
    dmgType=DamageType.Piercing,
    dmgMod=DamageMod.Strength,
    versatile=False,
    thrown=False, # Polearms are not typically thrown
    magical=False,
    ItemType=ItemType.Weapon,
    attunement=False
)

tornRags = Armor(
    name="Torn Rags",
    description="A ripped and worn-out outfit.",
    value=None,
    slot=Slots.Chest,
    grade="Light",
    ac=10, # Base AC for light armor without proficiency is 10 + Dex mod
    disadvantage=False, # Light armor usually doesn't give disadvantage
    dmgRes="None",
    magical=False,
    ItemType=ItemType.Armor,
    attunement=False
)

paper = Item(
    name="Paper",
    description="A blank piece of paper",
    value=None,
    magical=False,
    itemType=ItemType.Item,
    attunement=False
)


class Player:
    """Character Creation"""
    def __init__(self, name, gender, age, race, job):
        # Identity
        self.name = name
        self.gender = gender
        self.age = age
        self.race = race
        self.job = job

        # Defence
        self.ac = 0 # This will be calculated based on equipped armor
        self.elemental_resistance = {DamageType.Fire: False,
                                     DamageType.Cold: False,
                                     DamageType.Lightning: False,
                                     DamageType.Thunder: False,
                                     DamageType.Poison: False,
                                     DamageType.Acid: False,
                                     DamageType.Necrotic: False,
                                     DamageType.Radiant: False,
                                     DamageType.Force: False,
                                     DamageType.Psychic: False
                                     }
        self.physical_resistance = {DamageType.Slashing: False,
                                    DamageType.Bludgeoning: False,
                                    DamageType.Piercing: False}

        # Levels
        self.level = 1
        self.exp = 0
        self.maxEXP = 100

        # Equipment and Inventory
        self.inventory = Inventory() # Each player gets their own inventory instance

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

        # Initial items and equipment
        self.inventory.add_item(rock, 1)
        self.inventory.add_item(tornRags, 1)
        # Equip initial items (using the inventory's equip method)
        self.inventory.equip_item(rock, Slots.MainHand)
        self.inventory.equip_item(tornRags, Slots.Chest)


    def getModifier(self):
        """Floor calculation to work out skill check modifiers"""
        self.mods["Strength"] = -5 + self.stats["Strength"] // 2
        self.mods["Dexterity"] = -5 + self.stats["Dexterity"] // 2
        self.mods["Constitution"] = -5 + self.stats["Constitution"] // 2
        self.mods["Intelligence"] = -5 + self.stats["Intelligence"] // 2
        self.mods["Wisdom"] = -5 + self.stats["Wisdom"] // 2
        self.mods["Charisma"] = -5 + self.stats["Charisma"] // 2

    def set_stats_race(self):
        """Applies racial ability score increases."""
        # Access name attribute of Race object
        if self.race.name.lower() == "human":
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

        elif self.race.name.lower() == "elf":
            print("As an Elf, your dexterity increases by 2.")
            self.stats["Dexterity"] += 2
        elif self.race.name.lower() == "dwarf":
            print("As a Dwarf, your constitution increases by 2.")
            self.stats["Constitution"] += 2

    def set_stats_job(self):
        """Applies job-specific stats like hit points."""
        # Using self.job.name to access the job name from the Job object
        if self.job.name.lower() == "barbarian":
            self.hitDie = randint(self.job.hitdie[0], self.job.hitdie[1]) # Use job's hitdie range
            self.maxHP = (self.job.hitdie[1] + self.mods["Constitution"]) # Use max hitdie value for initial HP
            self.currentHP = self.maxHP
        elif self.job.name.lower() == "cleric":
            self.hitDie = randint(self.job.hitdie[0], self.job.hitdie[1])
            self.maxHP = (self.job.hitdie[1] + self.mods["Constitution"])
            self.currentHP = self.maxHP
        elif self.job.name.lower() == "wizard":
            self.hitDie = randint(self.job.hitdie[0], self.job.hitdie[1])
            self.maxHP = (self.job.hitdie[1] + self.mods["Constitution"])
            self.currentHP = self.maxHP

    def current_stats(self):
        """Prints a display of the user's current statistics."""
        print("Your current stats are:")
        print(f'Hit Points: {self.currentHP}/{self.maxHP}')
        print(f'Strength: {self.stats["Strength"]} ({self.mods["Strength"]:+})')
        print(f'Dexterity: {self.stats["Dexterity"]} ({self.mods["Dexterity"]:+})')
        print(f'Constitution: {self.stats["Constitution"]} ({self.mods["Constitution"]:+})')
        print(f'Intelligence: {self.stats["Intelligence"]} ({self.mods["Intelligence"]:+})')
        print(f'Wisdom: {self.stats["Wisdom"]} ({self.mods["Wisdom"]:+})')
        print(f'Charisma: {self.stats["Charisma"]} ({self.mods["Charisma"]:+})')

    def drop_item(self, item_name):
        """Drops an item from the player's inventory."""
        item_to_drop = None
        for item_obj in self.inventory.items:
            if item_obj.name.lower() == item_name.lower():
                item_to_drop = item_obj
                break
        if item_to_drop:
            self.inventory.remove_item(item_to_drop, count=1)
        else:
            print(f"You don't have '{item_name}' in your inventory.")

    def new_char(self):
        """Outputs final stats, armour, and inventory"""
        self.allocation()       # 1. Sets base self.stats from rolls.
        self.set_stats_race()   # 2. Applies racial bonuses to self.stats.
        self.getModifier()      # 3. Calculates ALL self.mods based on the FINAL self.stats (base + racial).
        self.set_stats_job()    # 4. Calculates maxHP using the now-accurate self.mods["Constitution"].
        self.current_stats()    # 5. Displays the final stats.
        print(' ')
        self.inventory.current_equipment() # Corrected to call instance method
        print(' ')
        self.inventory.current_inventory()
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
        """Handles the interactive allocation of rolled stats to attributes."""
        # Mapping for shorthand attribute names
        attribute_map = {
            "strength": "Strength", "str": "Strength",
            "dexterity": "Dexterity", "dex": "Dexterity",
            "constitution": "Constitution", "con": "Constitution",
            "intelligence": "Intelligence", "int": "Intelligence",
            "wisdom": "Wisdom", "wis": "Wisdom",
            "charisma": "Charisma", "cha": "Charisma"
        }

        while True:
            rolls = []
            stats = []
            attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
            while len(stats) != 6:
                # Roll 4d6, drop lowest
                four_d_six = sorted([randint(1, 6) for _ in range(4)])
                val = sum(four_d_six[1:]) # Sum the top 3
                stats.append(str(val))
                rolls = [] # Reset for next roll

            print(f"Please assign a stat to a selected attribute by entering the number then the attribute.\n"
                  f"For example, '10 strength' or '10 str' will assign 10 to your strength, if you have a 10 available.\n\n"
                  f"Your rolled stats are:\n {', '.join(stats)}\n\n"
                  f"Your attributes are:\n {', '.join(attributes)}\n")

            current_attributes = list(attributes)
            current_stats_to_assign = list(stats)

            # Reset player stats for new allocation attempt
            self.stats = {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}

            while len(current_stats_to_assign) > 0:
                input_text = input(">> ").lower().strip() # Convert to lower and strip whitespace
                words = input_text.split()

                if len(words) == 2:
                    chosen_stat_str = words[0]
                    chosen_attribute_input = words[1]

                    # Resolve shorthand to full attribute name
                    chosen_attribute_full = attribute_map.get(chosen_attribute_input, None)

                    if chosen_stat_str in current_stats_to_assign and chosen_attribute_full in current_attributes:
                        self.stats[chosen_attribute_full] = int(chosen_stat_str) # Assign, not add
                        current_stats_to_assign.remove(chosen_stat_str)
                        current_attributes.remove(chosen_attribute_full)
                        if len(current_stats_to_assign) == 0:
                            break # All stats assigned
                        print(f"The remaining stats are:\n {', '.join(current_stats_to_assign)}\n\n"
                              f"The remaining attributes are:\n {', '.join(current_attributes)}")
                    else:
                        print(
                            "Error. Either the number or attribute was not available/recognised. Please try again with 'Number' + 'Attribute'.")
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
                continue # Loop back to re-roll and re-allocate
            elif select == 'y':
                break
            else:
                print("Error. Input was not recognised. Please select 'Y' or 'N'.")
                # Loop back to ask again or handle as desired
