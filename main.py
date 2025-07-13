import sys
# Add the current directory to sys.path to allow imports from sibling files
sys.path.append('.')
# Import classes and functions from your existing files
from player import Player, Inventory
from function_list import startGame, parse, error_message, get_instructions
from job_list import Barbarian, Cleric, Wizard
from race_list import Elf, Dwarf, Human
from scene import *


class Engine:
    """
    The main game engine class to manage game state, current scene, and player.
    """
    def __init__(self):
        self.player = None  # Will be initialized after character creation
        self.current_scene = starting_clearing # Start the game in the starting clearing
        self.seed = self.current_scene.name # String representation of current scene name

    def set_player(self, player_obj):
        """Sets the main player object for the game."""
        self.player = player_obj

    def display_current_scene(self):
        """Prints the description of the current scene."""
        print(f"\n--- {self.current_scene.name} ---")
        print(self.current_scene.description)
        # Display available exits
        if self.current_scene.exits:
            exit_directions = ", ".join(self.current_scene.exits.keys()).title()
            print(f"Exits: {exit_directions}")
        # Display available items
        if self.current_scene.available_items:
            print("\nAround you, you see:")
            for item_obj, count in self.current_scene.available_items.items():
                if count > 0:
                    print(f"  - {item_obj.name} (x{count})")
        # Display lootable containers
        if self.current_scene.lootable_items:
            print("\nYou also notice some containers:")
            for container_name, items_in_container in self.current_scene.lootable_items.items():
                if any(count > 0 for count in items_in_container.values()): # Check if container has any items left
                    print(f"  - {container_name.title()}")


    def move_to_scene(self, direction):
        """
        Attempts to move the player to a new scene based on the direction.
        :param direction: The direction to move (e.g., "north", "east").
        """
        next_scene = self.current_scene.get_exit(direction)
        if next_scene:
            self.current_scene = next_scene
            self.seed = self.current_scene.name # Update the seed for the new scene
            self.display_current_scene()
        else:
            print("You can't go that way.")

    def examine_object(self, object_name):
        """
        Examines an object, either in the player's inventory or in the current scene.
        :param object_name: The name of the object to examine.
        """
        # Check player's inventory first
        found_in_inventory = False
        for item_obj, item_data in self.player.inventory.items.items():
            if object_name.lower() in item_obj.name.lower():
                print(f"\n--- {item_obj.name} ---")
                print(item_obj.description)
                if isinstance(item_obj, Weapon):
                    print(f"Damage: {item_obj.damage1H or item_obj.damage2H or item_obj.versatiledmg}")
                    print(f"Damage Type: {item_obj.dmgType.name.title()}")
                elif isinstance(item_obj, Armor):
                    print(f"AC: {item_obj.ac}")
                    print(f"Grade: {item_obj.grade}")
                print(f"Value: {item_obj.value if item_obj.value is not None else 'N/A'}")
                print(f"Magical: {item_obj.magical}")
                print(f"Attunement: {'Required' if item_obj.attunement else 'Not Required'}")
                found_in_inventory = True
                break

        if not found_in_inventory:
            # Check available items in the current scene
            found_in_scene = False
            for item_obj, count in self.current_scene.available_items.items():
                if object_name.lower() in item_obj.name.lower() and count > 0:
                    print(f"\n--- {item_obj.name} ---")
                    print(item_obj.description)
                    if isinstance(item_obj, Weapon):
                        print(f"Damage: {item_obj.damage1H or item_obj.damage2H or item_obj.versatiledmg}")
                        print(f"Damage Type: {item_obj.dmgType.name.title()}")
                    elif isinstance(item_obj, Armor):
                        print(f"AC: {item_obj.ac}")
                        print(f"Grade: {item_obj.grade}")
                    print(f"Value: {item_obj.value if item_obj.value is not None else 'N/A'}")
                    print(f"Magical: {item_obj.magical}")
                    print(f"Attunement: {'Required' if item_obj.attunement else 'Not Required'}")
                    found_in_scene = True
                    break

            if not found_in_scene:
                # Check lootable containers in the current scene
                found_in_loot = False
                for container_name, items_in_container in self.current_scene.lootable_items.items():
                    if object_name.lower() in container_name.lower(): # If user tries to examine the container itself
                        print(f"\nYou examine the {container_name}. Inside, you see:")
                        if items_in_container:
                            for item_obj, count in items_in_container.items():
                                if count > 0:
                                    print(f"  - {item_obj.name} (x{count})")
                        else:
                            print("It appears to be empty.")
                        found_in_loot = True
                        break # Exit after examining the container

                    for item_obj, count in items_in_container.items():
                        if object_name.lower() in item_obj.name.lower() and count > 0:
                            print(f"\n--- {item_obj.name} ---")
                            print(item_obj.description)
                            if isinstance(item_obj, Weapon):
                                print(f"Damage: {item_obj.damage1H or item_obj.damage2H or item_obj.versatiledmg}")
                                print(f"Damage Type: {item_obj.dmgType.name.title()}")
                            elif isinstance(item_obj, Armor):
                                print(f"AC: {item_obj.ac}")
                                print(f"Grade: {item_obj.grade}")
                            print(f"Value: {item_obj.value if item_obj.value is not None else 'N/A'}")
                            print(f"Magical: {item_obj.magical}")
                            print(f"Attunement: {'Required' if item_obj.attunement else 'Not Required'}")
                            found_in_loot = True
                            break
                    if found_in_loot:
                        break

                if not found_in_loot:
                    print(f"You don't see or have '{object_name}' to examine.")

    def take_item(self, item_name):
        """
        Attempts to take an item from the current scene and add it to the player's inventory.
        :param item_name: The name of the item to take.
        """
        found_item = False
        item_to_take = None
        for item_obj, count in self.current_scene.available_items.items():
            if item_name.lower() in item_obj.name.lower() and count > 0:
                item_to_take = item_obj
                found_item = True
                break

        if found_item:
            response = input(f'There are {self.current_scene.available_items[item_to_take]} {item_to_take.name} available.\n'
                             f'How many will you take? (enter "all" or a number)\n>> ').lower()

            if response == "0" or response == "none":
                print("You decide not to take any.")
            elif response == "all":
                self.player.inventory.add_item(item_to_take, self.current_scene.available_items[item_to_take])
                self.current_scene.remove_available_item(item_to_take, self.current_scene.available_items[item_to_take])
            elif response.isdigit():
                num_to_take = int(response)
                if num_to_take <= self.current_scene.available_items[item_to_take]:
                    self.player.inventory.add_item(item_to_take, num_to_take)
                    self.current_scene.remove_available_item(item_to_take, num_to_take)
                else:
                    print("You can't take more than exist.")
            else:
                print("Invalid input. Please enter 'all' or a number.")
        else:
            print("You don't see any of those lying around to take.")


    def loot_container(self, container_name):
        """
        Attempts to loot items from a container in the current scene.
        :param container_name: The name of the container to loot.
        """
        found_container = False
        container_items = {}
        for c_name, items_in_c in self.current_scene.lootable_items.items():
            if container_name.lower() in c_name.lower():
                container_items = items_in_c
                found_container = True
                break

        if found_container:
            if not container_items or all(count == 0 for count in container_items.values()):
                print(f"The {container_name} is empty.")
                return

            print(f"You look inside the {container_name}. You see:")
            loot_options = []
            for i, (item_obj, count) in enumerate(container_items.items()):
                if count > 0:
                    print(f"{i+1}) {item_obj.name} (x{count})")
                    loot_options.append((item_obj, count))
            print(f"{len(loot_options) + 1}) Take all")
            print(f"{len(loot_options) + 2}) Leave")

            while True:
                try:
                    choice = input("What would you like to take? (number or 'take all'/'leave')\n>> ").lower()
                    if choice == "leave":
                        print("You close the container.")
                        break
                    elif choice == "take all":
                        for item_obj, count in loot_options:
                            self.player.inventory.add_item(item_obj, count)
                            self.current_scene.remove_lootable_item(container_name, item_obj, count)
                        print(f"You took everything from the {container_name}.")
                        break
                    elif choice.isdigit():
                        index = int(choice) - 1
                        if 0 <= index < len(loot_options):
                            item_obj, count = loot_options[index]
                            self.player.inventory.add_item(item_obj, count)
                            self.current_scene.remove_lootable_item(container_name, item_obj, count)
                            print(f"You took the {item_obj.name}.")
                            # Re-display options if there's still loot
                            if any(c > 0 for c in container_items.values()):
                                print(f"Remaining items in {container_name}:")
                                for i, (item_obj, count) in enumerate(container_items.items()):
                                    if count > 0:
                                        print(f"{i+1}) {item_obj.name} (x{count})")
                                print(f"{len(loot_options) + 1}) Take all")
                                print(f"{len(loot_options) + 2}) Leave")
                            else:
                                print(f"The {container_name} is now empty.")
                                break
                        else:
                            print("Invalid selection.")
                    else:
                        print("Invalid input. Please enter a number, 'take all', or 'leave'.")
                except ValueError:
                    print("Invalid input. Please enter a number, 'take all', or 'leave'.")
        else:
            print("You don't see a container like that here to loot.")


# Initialize the game engine
game_engine = Engine()

def main_game_loop():
    """
    The main loop for the game, handling character creation and continuous gameplay.
    """
    # Character Creation
    name, gender, age, race, job = startGame()

    # Create player instance
    player = Player(name, gender, age, race, job)
    game_engine.set_player(player) # Set the player in the game engine

    # Display initial character summary
    player.new_char() # This calls allocation, which is interactive.

    print("\nYour adventure begins...")
    game_engine.display_current_scene() # Display the starting scene

    # Game loop
    while True:
        user_input = input("\nWhat do you do? >> ").lower()
        command, obj1 = parse(user_input)

        if command == "help":
            get_instructions()
        elif command == "scene":
            game_engine.display_current_scene()
        elif command == "inventory":
            game_engine.player.inventory.current_inventory()
        elif command == "equipment":
            Inventory.current_equipment() # This is a static method on Inventory class
        elif command == "stats":
            game_engine.player.current_stats()
        elif command == "hp":
            game_engine.player.health_check()
        elif command == "examine":
            if obj1:
                game_engine.examine_object(obj1)
            else:
                print("What would you like to examine?")
        elif command == "take":
            if obj1:
                game_engine.take_item(obj1)
            else:
                print("What would you like to take?")
        elif command == "loot":
            if obj1:
                game_engine.loot_container(obj1)
            else:
                print("What would you like to loot?")
        elif command == "drop":
            if obj1:
                game_engine.player.drop_item(obj1)
            else:
                print("What would you like to drop?")
        elif command.startswith("go "):
            direction = command.split(" ", 1)[1]
            game_engine.move_to_scene(direction)
        elif command == "quit":
            print("Thanks for playing!")
            break
        elif command == "error":
            error_message()
        else:
            print("Command not recognized. Type 'help' for a list of commands.")


if __name__ == "__main__":
    main_game_loop()

