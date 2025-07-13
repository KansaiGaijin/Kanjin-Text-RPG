import sys
# Add the current directory to sys.path to allow imports from sibling files
sys.path.append('.')

from player import Item, Weapon, Armor, rock, dagger, polearm, tornRags, paper, GP1, SP1, CP1
from enum_list import *

class Scene:
    """
    Represents a single location or area in the game.
    Each scene has a name, a description, and defines its exits to other scenes.
    It can also contain items that can be looted from containers/bodies or
    items that are simply available to be picked up.
    """
    def __init__(self, name, description, exits=None, lootable_items=None, available_items=None):
        self.name = name
        self.description = description
        # Exits are a dictionary mapping direction (str) to Scene objects
        self.exits = exits if exits is not None else {}
        # Lootable items are typically found within containers or on enemies.
        # Format: {"container_name": {item_obj: count, ...}, ...}
        self.lootable_items = lootable_items if lootable_items is not None else {}
        # Available items are items lying around in the scene.
        # Format: {item_obj: count, ...}
        self.available_items = available_items if available_items is not None else {}

    def __str__(self):
        """Returns the description of the scene."""
        return self.description

    def add_exit(self, direction, scene):
        """
        Adds an exit from this scene to another scene.
        :param direction: The direction (e.g., "north", "east") as a string.
        :param scene: The Scene object to link to.
        """
        self.exits[direction.lower()] = scene

    def get_exit(self, direction):
        """
        Returns the Scene object for a given direction, or None if no exit exists.
        :param direction: The direction to check.
        :return: The Scene object or None.
        """
        return self.exits.get(direction.lower())

    def add_lootable_item(self, container_name, item_obj, count=1):
        """
        Adds an item to a lootable container within the scene.
        :param container_name: The name of the container (e.g., "chest", "goblin corpse").
        :param item_obj: The Item object to add.
        :param count: The quantity of the item.
        """
        if container_name not in self.lootable_items:
            self.lootable_items[container_name] = {}
        self.lootable_items[container_name][item_obj] = self.lootable_items[container_name].get(item_obj, 0) + count

    def add_available_item(self, item_obj, count=1):
        """
        Adds an item that is freely available in the scene.
        :param item_obj: The Item object to add.
        :param count: The quantity of the item.
        """
        self.available_items[item_obj] = self.available_items.get(item_obj, 0) + count

    def remove_available_item(self, item_obj, count=1):
        """
        Removes a specified count of an available item from the scene.
        :param item_obj: The Item object to remove.
        :param count: The quantity to remove.
        """
        if item_obj in self.available_items:
            self.available_items[item_obj] -= count
            if self.available_items[item_obj] <= 0:
                del self.available_items[item_obj]

    def remove_lootable_item(self, container_name, item_obj, count=1):
        """
        Removes a specified count of an item from a lootable container in the scene.
        :param container_name: The name of the container.
        :param item_obj: The Item object to remove.
        :param count: The quantity to remove.
        """
        if container_name in self.lootable_items and item_obj in self.lootable_items[container_name]:
            self.lootable_items[container_name][item_obj] -= count
            if self.lootable_items[container_name][item_obj] <= 0:
                del self.lootable_items[container_name][item_obj]
                if not self.lootable_items[container_name]: # If container is empty, remove it
                    del self.lootable_items[container_name]


# --- Default Scenes ---
# Scene 0: Tutorial
tutorial = Scene(
    name="Tutorial",
    description="Welcome to Kanjin Text RPG!\n\n"
                "This is a very simple tutorial to show you the basics of issuing commands.\n"
                "Important commands you'll want to know can be found by typing 'Help'.\n\n"
                "These are the available commands:\n"
                "Help - Prints this help message.\n"
                "Check inventory | bag | backpack - Lists items you are carrying.\n"
                "    Can also just enter 'inventory | bag | backpack\n" 
                "Check equipment | equipped | items - Lists items you have equipped\n"
                "    Can also just enter 'equipment | equipped | items\n" 
                "Check stats or Check hitpoints | hp | health - Shows your stat block or current health details\n"
                "    Can also just enter 'stats | health | hitpoints | hp\n" 
                "Go *direction* - Each scene will give you available directions i.e North\n"
                "Enter cave | house | room - maybe... TBC\n"
                "Scene or Location - Replays the current area's details\n"
                "Look around - lists the available items in your scene without displaying the scene description.\n"
                "Examine | Open | Loot *object* - Provides details of an item, opens a container, or takes an object."
)
tutorial.add_available_item(rock, 1)
tutorial.add_available_item(paper, 2)
tutorial.add_lootable_item("suspicious tree trunk", Item("Test Item",
                                                         "This is for testing purposes", None,
                                                         False, ItemType.Item, False), 1)

# Scene 1: Starting Clearing
starting_clearing = Scene(
    name="Starting Clearing",
    description="You are in a small clearing, surrounded by tall, ancient trees. "
                "A faint, overgrown path leads north, and a darker, narrower trail goes east. "
                "Sunlight filters through the canopy, dappling the forest floor. "
                "You notice a small, weathered wooden chest near a fallen log."
)
starting_clearing.add_available_item(rock, 3) # Rocks lying on the ground
starting_clearing.add_lootable_item("small wooden chest", GP1, 15)
starting_clearing.add_lootable_item("small wooden chest", SP1, 20)


# Scene 2: Forest Path
forest_path = Scene(
    name="Forest Path",
    description="The path winds deeper into the whisper-quiet forest. The trees here are "
                "ancient and gnarled, their branches intertwining overhead, creating a dense canopy. "
                "The air is thick with the scent of pine needles and damp earth. "
                "You hear the distant caw of a crow. The clearing is to the south."
)
forest_path.add_available_item(dagger, 1) # A lone dagger dropped on the path


# Scene 3: Dark Cave Entrance
dark_cave_entrance = Scene(
    name="Dark Cave Entrance",
    description="The narrow trail ends abruptly at the jagged mouth of a dark, foreboding cave. "
                "A chilling, damp wind blows from within, carrying the faint smell of mildew and something else... "
                "something ancient. The entrance is shrouded in thick vines. "
                "The clearing is to the west."
)
dark_cave_entrance.add_available_item(polearm, 1) # A polearm leaning against the cave wall


# Link the scenes together
tutorial.add_exit("exit", starting_clearing)

starting_clearing.add_exit("north", forest_path)
starting_clearing.add_exit("east", dark_cave_entrance)

forest_path.add_exit("south", starting_clearing)

dark_cave_entrance.add_exit("west", starting_clearing)

# Global map for easy scene access (optional, could also be managed by an Engine class)
Map = {
    "Starting Clearing": starting_clearing,
    "Forest Path": forest_path,
    "Dark Cave Entrance": dark_cave_entrance,
    "Tutorial": tutorial,
}

