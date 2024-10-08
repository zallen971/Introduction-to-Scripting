"""
Zachary Allen
IT:140 - Introduction to Scripting
Text Based Game
Title: The Wizard's Will
____________________________________

Player must collect the 5 power source items scattered throughout the castle in order to
beat the Grand Wizard hiding in the Crystal Caverns

If they don't have all items they stand no chance, and it's an immediate defeat!

For debugging purposes - left, down, up, right, up, down, down, down, up, up, right, right, down, down
The speed run for each item then to the Grand Wizard hiding in the Crystal Caverns
"""
import random


# Introduction function
def introduction():
    print("The Wizard's Will")
    print("The object is to collect 5 power source items to beat the grand wizard")
    print("Movement Commands: 'up', 'down', 'right', 'left', 'location' to "
          "see your current room, and 'exit' to quit the game")
    print("To add the power source item to inventory: p")
    print("________________________________________________________________")


# Gameplay: movement command , current/new room, inventory, grand wizard check
def gameplay(current_room, rooms, inventory, player_health, wizard_health):
    movement_command = input("What is your movement command: ")
    print()
    new_room = ''
    # if the player enters 'pick up item' it adds item to inventory and deletes it from the current room
    if movement_command == 'p':
        if 'item' in rooms[current_room]:
            item_name = rooms[current_room]["item"]
            inventory.append(item_name)
            print(f"Way to go, you picked up the {item_name}. That's sure to come in handy!\n")
            del rooms[current_room]['item']
        else:
            print("No item in this room, you can tell.")
        return current_room

    # Movement commands for the player, also handles the exit and location, and invalid command
    if movement_command in rooms[current_room]:
        new_room = rooms[current_room][movement_command]

        # Check if new room is None
        if new_room is None:
            print("There's no room in that direction.")
            return current_room
    elif movement_command == 'exit':
        print('Exiting the game...')
        exit()
    elif movement_command == 'location':
        print(f"You're current location is: {current_room}")
        return current_room
    else:
        print("Invalid movement command, must enter: up, down, right, left, p, location, exit")
        return current_room

    # lets the player know they moved to a new room
    if new_room:
        print(f'You moved from {current_room} to {new_room}')

        # prints a description of the room
        if new_room and new_room in rooms and 'description' in rooms[new_room]:
            print(f"\n{rooms[new_room]['description']}\n")

            '''lets the player know that if there is an item in the room 
            they entered or not or if the grand wizard is in there'''
            if 'enemy' in rooms[new_room]:
                print("The Grand Wizard is in this room!")
                if len(inventory) == 7:
                    print("You are ready to battle the Grand Wizard!\n")
                    battle_sequence(player_health, wizard_health)
                    exit()
                elif len(inventory) < 7:
                    print("You don't have the power and the Grand Wizard one shot you!")
                    print("Game Over!!")
                    exit()
            elif 'item' in rooms[new_room]:
                print(
                    f"You feel the aura shift and see that there is the {rooms[new_room]['item']} in here, you should pick it up!\n")
            else:
                print("\nNo item in this room, you can tell.")

        return new_room


# function to display the inventory for the player and joins the items together to display
def display_inventory(inventory):
    if inventory:
        print("Your inventory: ", ", ".join(inventory))
    else:
        print("You don't have any items yet.\n")


# battle sequence function
def battle_sequence(player_health, wizard_health):
    # while both the player and wizard health are greater than 0 loop
    while player_health > 0 and wizard_health > 0:
        # gets a random attack power number between 0-20
        player_attack = random.randint(0, 20)
        wizard_attack = random.randint(0, 20)

        print(f"\nYou attack the Grand Wizard for {player_attack} damage")
        # sets it so the wizard health doesn't go into negative numbers
        wizard_health = max(wizard_health - player_attack, 0)
        print(f"The wizard has {wizard_health} health points left!\n")

        if wizard_health == 0:
            print("Congratulations, you have defeated the Grand Wizard and won the game!"
                  " Your will is strong and nobody can compare!")
            print("Reclaim the castle and bring wisdom, stability, and peace back into the lands!")
            return True

        print(f"The Grand Wizard attacked you for {wizard_attack} damage")
        # sets it so the player health doesn't go into the negative numbers
        player_health = max(player_health - wizard_attack, 0)
        print(f"You have {player_health} health points left!")

        if player_health == 0:
            print("You were not strong enough to beat the Grand Wizard!")
            exit()

        # asks the player to hit enter to continue battle sequence, makes it easier to follow
        input("Press Enter to continue...")


# dictionary to link each room and item. Crystal Cavern contains the Grand Wizard as well
def main():
    # Defines the rooms dictionary
    rooms = {
        'Sanctuary': {'up': 'The Whispering Gallery', 'right': 'Citadel',
                      'down': 'The Moonlit Garden', 'left': 'The Emerald Labyrinth'},  # Main entrance room

        'The Whispering Gallery': {'down': 'Sanctuary', 'up': None, 'right': None, 'left': None,
                                   'item': 'Boots of the Flamewalker',
                                   'description': 'The walls are adorned with intricate tapestries from '
                                                  'the legends of old.'
                                   },  # Boots of Flamewalker

        'Citadel': {'left': 'Sanctuary', 'right': 'Tower', 'item': 'Spell Book of the Dead',
                    'up': None, 'down': None, 'description':
                        'You can tell this room was an important one in the days of old. '
                        'Likely where the fate of the kingdom was decided.'
                    },  # Book of the dead

        'The Moonlit Garden': {'up': 'Sanctuary', 'down': 'The Forgotten Chamber',
                               'left': None, 'right': None,
                               'description': 'The room is bathed in the soft glow of the moonlight.'
                               },  # empty room

        'Tower': {'left': 'Citadel', 'down': 'The Keep', 'item': 'Staff of Ancients',
                  'up': None, 'right': None,
                  'description': 'A place of solitude and mystery.It feels like a place of strength and isolation.'
                  },  # Staff of Ancients

        'The Keep': {'up': 'Tower', 'down': 'Crystal Cavern', 'item': 'Heart of a Dragon',
                     'right': None, 'left': None,
                     'description': 'crumbling furniture and structure, a place that once stood for the strength,'
                                    ' protection, and resilience of its people.'
                     },  # Heart of a Dragon

        'The Emerald Labyrinth': {'right': 'Sanctuary', 'down': 'Shadowed Hall', 'item': 'Orb of Elements',
                                  'up': 'The Archmage Sanctum', 'left': None,
                                  'description': 'Emerald crystals shimmering, there are so many locked doors in here.'
                                  },  # Orb of Elements

        'Shadowed Hall': {'up': 'The Emerald Labyrinth', 'item': 'Amulet of Protection',
                          'right': None, 'left': None, 'down': None,
                          'description': 'Dark and cold hall seemingly stretched endlessly,'
                                         ' little light coming from the torches adorned on the walls.'},  # Amulet of Protection

        'The Forgotten Chamber': {'up': 'The Moonlit Garden', 'item': 'Soul Reaver Sword', 'right': None, 'left': None,
                                  'down': None, 'description': 'The room has been long forgotten, shrouded in darkness.'
                                  },  # Soul Reaver Sword

        'The Archmage Sanctum': {'down': 'The Emerald Labyrinth', 'up': None,
                                 'left': None, 'right': None,
                                 'description': 'Ancient tomes sprawled on a desk, the smell of incense overtaking the air.'
                                 },  # empty room

        'Crystal Cavern': {'up': 'The Keep', 'enemy': 'Grand Wizard', 'right': None,
                           'down': None, 'left': None, 'description': None}  # The enemy room - Grand Wizard
    }

    introduction()
    inventory = []
    player_health = 100
    wizard_health = 100
    current_room = 'Sanctuary'
    print(f"\nYou have arrived at the castle. You are in the main room {current_room}. Which way should you go?")
    print("You don't have any items yet.")

    # while loop to handle the game
    while True:
        # calls the player command function
        current_room = gameplay(current_room, rooms, inventory, player_health, wizard_health)

        # calls the display inventory function
        display_inventory(inventory)


if __name__ == '__main__':
    main()
