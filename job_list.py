class Job:
    def __init__(self, name, description, hitdie, proficiency, savingthrow, skill, gold):
        self.name = name
        self.description = description
        self.hitdie = hitdie
        self.proficiency = proficiency
        self.savingthrow = savingthrow
        self.skill = skill
        self.gold = gold

    def __repr__(self) -> str:
        profs = ""
        for key, value in self.proficiency.items():
            profs = profs + f"{key.title()}: {', '.join(value).title()}" + "\n"

        return f"{self.description}\n\n" \
               f"{self.name}'s have the following traits:\n\n" \
               f"Hit Die\n" \
               f"1d{self.hitdie[1]}\n\n" \
               f"Proficiencies\n" \
               f"{profs}\n" \
               f"Saving Throws\n" + '\n'.join(self.savingthrow).title() + f"\n\n" \
               f"Choose {str(self.skill[0])} of the following skills:\n" \
               + '\n'.join(self.skill[1:]).title() + '\n'


class Barbarian(Job):
    def __init__(self):
        name = "Barbarian"
        description = "A tall human tribesman strides through a blizzard, draped in fur and hefting his axe. " \
                      "He laughs as he charges toward the frost giant who dared poach his people’s elk herd.\n" \
                      "A half-orc snarls at the latest challenger to her authority over their savage tribe, ready to " \
                      "break his neck with her bare hands as she did to the last six rivals.\n" \
                      "Frothing at the mouth, a dwarf slams his helmet into the face of his drow foe, then turns to" \
                      " drive his armored elbow into the gut of another.\n" \
                      "These barbarians, different as they might be, are defined by their rage: unbridled, " \
                      "unquenchable, and unthinking fury. More than a mere emotion, their anger is the\n" \
                      "ferocity of a cornered predator, the unrelenting assault of a storm, " \
                      "the churning turmoil of the sea.\n" \
                      "For some, their rage springs from a communion with fierce animal spirits. Others draw from a " \
                      "roiling reservoir of anger at a world full of pain. For every barbarian,\n" \
                      "rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, " \
                      "and feats of strength."
        hitdie = [1, 12]
        proficiency = {
            "armor": [
                "light",
                "medium",
                "shields"
            ],
            "weapons": [
                "simple",
                "martial"
            ],
            "tools": [
            ]
        }
        savingthrow = [
            "strength",
            "constitution"
        ]
        skills = [
                2,
                "animal handling",
                "athletics",
                "intimidation",
                "nature",
                "perception",
                "survival"
            ]
        gold = [2, 10]
        super().__init__(name, description, hitdie, proficiency, savingthrow, skills, gold)


class Cleric(Job):
    def __init__(self):
        name = "Cleric"
        description = "Arms and eyes upraised toward the sun and a prayer on his lips, an elf begins to glow with " \
                      "an inner light that spills out to heal his battle-worn companions.\n" \
                      "Chanting a song of glory, a dwarf swings his axe in wide swaths to cut through the ranks of " \
                      "orcs arrayed against him, shouting praise to the gods with every foe’s fall.\n" \
                      "Calling down a curse upon the forces of undeath, a human lifts her holy symbol as light " \
                      "pours from it to drive back the zombies crowding in on her companions.\n" \
                      "Clerics are intermediaries between the mortal world and the distant planes of the gods. " \
                      "As varied as the gods they serve, clerics strive to embody the handiwork of their deities.\n" \
                      "No ordinary priest, a cleric is imbued with divine magic."
        hitdie = [1, 8]
        proficiency = {
            "armor": [
                "light",
                "medium",
                "shields"
            ],
            "weapons": [
                "simple"
            ],
            "tools": [
                ""
            ]
        }
        savingthrow = [
            "wisdom",
            "charisma"
        ]
        skill = [
                2,
                "history",
                "insight",
                "medicine",
                "persuasion",
                "religion"
            ]
        gold = [2, 10]
        super().__init__(name, description, hitdie, proficiency, savingthrow, skill, gold)


class Wizard(Job):
    def __init__(self):
        name = "Wizard"
        description = "Clad in the silver robes that denote her station, an elf closes her eyes to shut out the " \
                      " noise of the battlefield and begins her quiet chant. Fingers weaving in front of her, she\n" \
                      "completes her spell and launches a tiny bead of fire toward the enemy ranks, where it erupts " \
                      "into a conflagration that engulfs the soldiers.\n" \
                      "Checking and rechecking his work, a human scribes an intricate magic circle in chalk on the" \
                      " bare stone floor, then sprinkles powdered iron along every line and graceful curve.\n" \
                      "When the circle is complete, he drones a long incantation. A hole opens in space inside " \
                      "the circle, bringing a whiff of brimstone from the otherworldly plane beyond.\n" \
                      "Crouching on the floor in a dungeon intersection, a gnome tosses a handful of small bones " \
                      "inscribed with mystic symbols, muttering a few words of power over them. Closing his eyes \n" \
                      "to see the visions more clearly, he nods slowly, then opens his eyes and points down " \
                      "the passage to his left.\n" \
                      "Wizards are supreme magic-users, defined and united as a class by the spells they cast. " \
                      "Drawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of\n" \
                      "explosive fire, arcing lightning, subtle deception, and brute-force mind control. Their magic " \
                      "conjures monsters from other planes of existence, glimpses the future, or turns slain foes\n" \
                      "into zombies. Their mightiest spells change one substance into another, call meteors down " \
                      "from the sky, or open portals to other worlds."
        hitdie = [1, 6]
        proficiency = {
            "armor": [
                ""
            ],
            "weapons": [
                "daggers",
                "darts",
                "slings",
                "quarterstaffs",
                "light crossbows"
            ],
            "tools": [
                ""
            ]
        }
        savingthrow = [
            "intelligence",
            "wisdom"
        ]
        skills = [
                2,
                "arcana",
                "history",
                "insight",
                "investigation",
                "medicine",
                "religion"
            ]
        gold = [2, 10]
        super().__init__(name, description, hitdie, proficiency, savingthrow, skills, gold)


Barbarian = Barbarian()
Cleric = Cleric()
Wizard = Wizard()
