from enum import Enum, auto

class DamageType(Enum):
    # Physical
    Slashing = auto()
    Piercing = auto()
    Bludgeoning = auto()
    # Magical
    Cold = auto()
    Fire = auto()
    Lightning = auto()
    Thunder = auto()
    Poison = auto()
    Acid = auto()
    Necrotic = auto()
    Radiant = auto()
    Force = auto()
    Psychic = auto()


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
    Other = auto()
    Attunement = auto()