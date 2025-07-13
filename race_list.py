class Race:
    def __init__(self, name, name_adjective, description, asi, speed, darkvision,
                 language, advantage, resistance, proficiency, traits):
        self.name = name
        self.name_adjective = name_adjective
        self.description = description
        self.asi = asi
        self.speed = speed
        self.darkvision = darkvision
        self.language = language
        self.advantage = advantage
        self.resistance = resistance
        self.proficiency = proficiency
        self.traits = traits

    def __repr__(self) -> str:
        traits = ""
        for k, v in self.traits.items():
            traits = traits + f'{k}:\n' \
                     f'{v}\n\n'

        return f'{self.description}' \
               f'{self.name_adjective} have the following traits:\n\n' \
               f'{traits}'


class Elf(Race):
    def __init__(self):
        name = "Elf"
        name_adjective = "Elven"
        description = "Elves are a magical people of otherworldly grace, living in the world but not entirely part\n" \
                      "of it. They live in places of ethereal beauty, in the midst of ancient forests or in silvery\n" \
                      "spires glittering with faerie light, where soft music drifts through the air\n" \
                      "and gentle fragrances waft on the breeze. Elves love nature and magic, art and artistry,\n" \
                      "music and poetry, and the good things of the world.\n\n"
        asi = {
            'Dexterity': 2
        }
        speed = {
            'Walking': 30
        }
        darkvision = [30, 60]
        language = ["Common", "Elvish"]
        advantage = []
        resistance = []
        proficiency = ["Perception"]
        traits = {"Ability Score Increase": "Your Dexterity Score increases by 2",
                  "Age": "Although elves reach physical maturity at about the same age as humans, the elven\n"
                         "understanding of adulthood goes beyond physical growth to encompass worldly experience.\n"
                         "An elf typically claims adulthood and an adult name around the age of 100 and can live to"
                         " be 750 years old.",
                  "Size": "Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.",
                  "Speed": "Your base walking speed is 30.",
                  "Darkvision": "Accustomed to twilit forests and the night sky, you have superior vision in dark and\n"
                                "dim conditions. You can see in dim light within 60 feet of you as if it were bright\n"
                                "light, and in darkness as if it were dim light. You can’t discern color in darkness,\n"
                                "only shades of gray.",
                  "Keen Senses": "You have proficiency in the Perception skill.",
                  "Fey Ancestry": "You have advantage on saving throws against being charmed, "
                                  "and magic can’t put you to sleep.",
                  "Trance": "Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for\n"
                            "4 hours a day. (The Common word for such meditation is “trance.”) While meditating,\n"
                            "you can dream after a fashion; such dreams are actually mental exercises that have\n"
                            "become reflexive through years of practice. After resting in this way, you gain the\n"
                            "same benefit that a human does from 8 hours of sleep.",
                  "Languages": "You can speak, read, and write Common and Elvish. Elvish is fluid, with subtle\n"
                               "intonations and intricate grammar. Elven literature is rich and varied, and their\n"
                               "songs and poems are famous among other races. Many bards learn their language so they\n"
                               "can add Elvish ballads to their repertoires."
                  }
        super().__init__(name, name_adjective, description, asi, speed, darkvision,
                         language, advantage, resistance, proficiency, traits)


class Dwarf(Race):
    def __init__(self):
        name = "Dwarf"
        name_adjective = "Dwarven"
        description = "Kingdoms rich in ancient grandeur, halls carved into the roots of\n" \
                      "mountains, the echoing of picks and hammers in deep mines and blazing\n" \
                      "forges, a commitment to clan and tradition, and a burning hatred of goblins and orcs—these\n" \
                      "common threads unite all dwarves.\n\n"
        asi = {
            'Constitution': 2
        }
        speed = {
            'Walking': 25
        }
        darkvision = [30, 60]
        language = ["Common", "Dwarvish"]
        advantage = ["Poison"]
        resistance = ["Poison"]
        proficiency = ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"]
        traits = {"Ability Score Increase": "Your Constitution score increases by 2.",
                  "Age": "Dwarves mature at the same rate as humans, but they’re considered young until they reach\n"
                         "the age of 50. On average, they live about 350 years.",
                  "Size": "Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.",
                  "Speed": "Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.",
                  "Darkvision": "Accustomed to life underground, you have superior vision in dark and dim conditions\n"
                                "You can see in dim light within 60 feet of you as if it were bright light, and in\n"
                                "darkness as if it were dim light. You can’t discern color in darkness, only shades"
                                " of gray.",
                  "Dwarven Resilience": "You have advantage on saving throws against poison, and you have resistance "
                                        "against poison damage.",
                  "Dwarven Combat Training": "You have proficiency with the battleaxe, handaxe, light hammer, "
                                             "and warhammer.",
                  "Tool Proficiency": "You gain proficiency with the artisan’s tools of your choice: smith’s tools, "
                                      "brewer’s supplies, or mason’s tools.",
                  "Stone Cutting": "Whenever you make an Intelligence (History) check related to the origin of\n"
                                   "stonework, you are considered proficient in the History skill and add double your\n"
                                   "proficiency bonus to the check, instead of your normal proficiency bonus.",
                  "Languages": "You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard\n"
                               "consonants and guttural sounds, and those characteristics spill over into whatever"
                               "other language a dwarf might speak."
                  }
        super().__init__(name, name_adjective, description, asi, speed, darkvision,
                         language, advantage, resistance, proficiency, traits)


class Human(Race):
    def __init__(self):
        name = "Human"
        name_adjective = "Human"
        description = "In the reckonings of most worlds, humans are the youngest of the common races, late to arrive " \
                      "on the world scene and short-lived in comparison to dwarves, elves, and dragons. Perhaps it\n" \
                      "is because of their shorter lives that they strive to achieve as much as they can in the " \
                      "years they are given. Or maybe they feel they have something to prove to the elder races,\n" \
                      "and that’s why they build their mighty empires on the foundation of conquest and trade. " \
                      "Whatever drives them, humans are the innovators, the achievers, and the pioneers " \
                      "of the worlds.\n\n"
        asi = {
        }
        speed = {
            'Walking': 30
        }
        darkvision = [0, 0]
        language = ["Common"]
        advantage = []
        resistance = []
        proficiency = []
        traits = {"Ability Score Increase": "Two different ability scores of your choice increase by 1.",
                  "Age": "Humans reach adulthood in their late teens and live less than a century.",
                  "Size": "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. "
                          "Regardless of your position in that range, your size is Medium.",
                  "Speed": "Your base walking speed is 30 feet.",
                  "Skills": "You gain proficiency in one skill of your choice.",
                  "Feat": "You gain one feat of your choice.",
                  "Languages": "You can speak, read, and write Common and one extra language of your choice. "
                               "Humans typically learn the languages of other peoples they deal with, including\n"
                               "obscure dialects. They are fond of sprinkling their speech with words borrowed from "
                               "other tongues: Orc curses, Elvish musical expressions,\n"
                               "Dwarvish military phrases, and so on."
                  }
        super().__init__(name, name_adjective, description, asi, speed, darkvision,
                         language, advantage, resistance, proficiency, traits)


Elf = Elf()
Dwarf = Dwarf()
Human = Human()
