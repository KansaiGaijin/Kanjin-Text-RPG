import sys
# Add the current directory to sys.path to allow imports from sibling files
sys.path.append('.')
from player import Player
from function_list import startGame, parse, error_message, get_instructions
from scene import *


class Engine:
    """
    The main game engine class to manage game state, current scene, and player.
    """
    def __init__(self):
        self.player = None  # Will be initialized after character creation
        self.current_scene = tutorial # Start the game in the tutorial
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
            print("\nYou also notice:")
            for container_name, items_in_container in self.current_scene.lootable_items.items():
                if any(count > 0 for count in items_in_container.values()): # Check if container has any items left
                    print(f"  - {container_name.title()}")

    def look_around(self):
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
            print("\nYou also notice:")
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
                    print(f"Value: {item_obj.value if item_obj.value is not None else 'No value'}")
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
        """Allows the player to loot items from a specified container."""
        container_found = False
        for current_container_name, items_in_container in list(self.current_scene.lootable_items.items()):
            if current_container_name.lower() == container_name.lower():
                container_found = True
                if not items_in_container:
                    print(f"The {container_name} is empty.")
                    return

                print(f"You look inside the {container_name}. You see:")
                loot_list = list(items_in_container.items())  # List of (item_obj, count) tuples

                while True:
                    for i, (item_obj, count) in enumerate(loot_list, 1):
                        print(f"{i}) {item_obj.name} (x{count})")

                    # Dynamically determine the numbers for "Take all" and "Leave"
                    take_all_option = len(loot_list) + 1
                    leave_option = len(loot_list) + 2

                    print(f"{take_all_option}) Take all")
                    print(f"{leave_option}) Leave")

                    choice = input("What would you like to take? (number or 'take all'/'leave')\n>> ").lower().strip()

                    # --- MODIFIED LOGIC START ---
                    if choice == "take all" or (choice.isdigit() and int(choice) == take_all_option):
                        for item_obj, count in list(items_in_container.items()):
                            self.player.inventory.add_item(item_obj, count)
                            print(f"- Took {count} {item_obj.name}")
                            del items_in_container[item_obj]
                        print(f"The {container_name} is now empty.")
                        return
                    elif choice == "leave" or (choice.isdigit() and int(choice) == leave_option):
                        print(f"You leave the {container_name} untouched.")
                        return
                    else:  # Now this 'else' only deals with potential item selections
                        try:
                            selection_index = int(choice) - 1
                            if 0 <= selection_index < len(loot_list):
                                item_obj, current_count = loot_list[selection_index]
                                take_count_input = input(
                                    f"How many {item_obj.name} will you take? (enter 'all' or a number)\n>> ").lower().strip()

                                if take_count_input == "all":
                                    take_count = current_count
                                else:
                                    try:
                                        take_count = int(take_count_input)
                                    except ValueError:
                                        print("Invalid amount. Please enter 'all' or a number.")
                                        continue  # Go back to the main loot menu

                                if take_count > 0 and take_count <= current_count:
                                    self.player.inventory.add_item(item_obj, take_count)
                                    items_in_container[item_obj] -= take_count
                                    print(f"You took {take_count} {item_obj.name}.")

                                    if items_in_container[item_obj] <= 0:
                                        del items_in_container[item_obj]
                                        loot_list = list(items_in_container.items())  # Rebuild loot_list

                                    if not items_in_container:
                                        print(f"The {container_name} is now empty.")
                                        return
                                    elif not loot_list:  # This handles if all items were individually taken and loot_list becomes empty
                                        print(f"The {container_name} is now empty.")
                                        return
                                else:
                                    print("Invalid amount or not enough items.")
                            else:
                                print("Invalid selection. Please choose a valid item number, 'take all', or 'leave'.")
                        except ValueError:
                            print("Invalid selection. Please enter a number, 'take all', or 'leave'.")
                    # --- MODIFIED LOGIC END ---
                # This return is unreachable if the while True loop has a return path for all conditions
                # but it doesn't hurt as a safeguard if logic changes later.
                return

        if not container_found:
            print(f"You don't see a '{container_name}' here to loot.")


# Initialize the game engine
game_engine = Engine()

def main_game_loop():
    """
    The main loop for the game, handling character creation and continuous gameplay.
    """
    # Character Creation
    name, gender, age, race, job, pre_allocated_stats = startGame()

    # Create player instance
    player = Player(name, gender, age, race, job)
    game_engine.set_player(player) # Set the player in the game engine

    # Display initial character summary
    if pre_allocated_stats is None:
        # For 'Create New Character' or 'Quick Set Up'
        game_engine.player.new_char()
    else:
        # For 'Pre-generated Character'
        game_engine.player.stats = pre_allocated_stats
        game_engine.player.getModifier()
        game_engine.player.set_stats_job()  # Still need to set HP based on job and Con modifier
        game_engine.player.current_stats()  # Display stats after setting them
        print(' ')
        game_engine.player.inventory.current_equipment()
        print(' ')
        game_engine.player.inventory.current_inventory()
        print(' ')

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
        elif command == "look_around":
            game_engine.look_around()
        elif command == "inventory":
            game_engine.player.inventory.current_inventory()
        elif command == "equipment":
            game_engine.player.inventory.current_equipment()
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
        elif command == "go":
            direction = obj1
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

