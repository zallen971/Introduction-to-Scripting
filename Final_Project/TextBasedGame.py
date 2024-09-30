"""
Zachary Allen
IT:140 - Introduction to Scripting
Text Based Game
The Wizard's Will
____________________________________

Player must collect the 5 power source items scattered throughout the castle in order to
beat the Grand Wizard hiding in the Crystal Caverns

If they don't have all items they stand no chance, and it's an immediate defeat!

For debugging purposes - left, down, up, right, right, right, down, down
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
        item_name = rooms[current_room]["item"]
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == item_name:
            inventory.append(item_name)
            print(f"Way to go, you picked up the {item_name}. That's sure to come in handy!\n")
            del rooms[current_room]['item']
        else:
            print("No item in this room, you can tell.")
        return current_room

    # Movement commands for the player, also handles the exit command and location command
    if movement_command == "up":
        new_room = rooms[current_room]["up"]
    elif movement_command == "down":
        new_room = rooms[current_room]["down"]
    elif movement_command == "right":
        new_room = rooms[current_room]["right"]
    elif movement_command == "left":
        new_room = rooms[current_room]["left"]
    elif movement_command == "exit":
        exit()
    elif movement_command == "location":
        print(f"You're current location is: {current_room}")
        return current_room
    else:
        print("Invalid movement command, must enter: up, down, right, left, location, exit")

    """ lets player know they moved from the current room to a new one 
    then sets new room as current room, also checks for Grand Wizard in room 
    and checks if player has all 5 items or not to determine outcome"""
    if new_room:
        print(f"You moved from {current_room} to {new_room}!\n")

        # lets the player know that if there is an item in the room they entered or not or if the grand wizard is in there
        if 'enemy' in rooms[new_room]:
            print("The Grand Wizard is in this room!")
            if len(inventory) == 5:
                print("You are ready to battle the Grand Wizard!\n")
                battle_sequence(player_health, wizard_health)
                exit()
            elif len(inventory) < 5:
                print("You don't have the power and the Grand Wizard one shot you!")
                print("Game Over!!")
                exit()
        elif 'item' in rooms[new_room]:
            print(
                f"You feel the aura shift and see that there is the {rooms[new_room]['item']} in here, you should pick it up!\n")
        else:
            print("No item in this room, you can tell.")
        return new_room

    # Lets player know there isn't a room in the direction if there is none according to rooms dictionary
    else:
        print("There is no room that way.")
        return current_room


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
                      'down': 'The Forgotten Chamber', 'left': 'The Emerald Labyrinth'},
        'The Whispering Gallery': {'down': 'Sanctuary', 'up': None, 'right': None, 'left': None},
        'Citadel': {'left': 'Sanctuary', 'right': 'Tower', 'item': 'Spell Book of the Dead',
                    'up': None, 'down': None, },
        'Tower': {'left': 'Citadel', 'down': 'The Keep', 'item': 'Staff of Ancients',
                  'up': None, 'right': None},
        'The Keep': {'up': 'Tower', 'down': 'Crystal Cavern', 'item': 'Heart of a Dragon',
                     'right': None, 'left': None},
        'The Emerald Labyrinth': {'right': 'Sanctuary', 'down': 'Shadowed Hall', 'item': 'Orb of Elements',
                                  'up': None, 'left': None},
        'Shadowed Hall': {'up': 'The Emerald Labyrinth', 'item': 'Amulet of Protection',
                          'right': None, 'left': None, 'down': None},
        'Crystal Cavern': {'up': 'The Keep', 'enemy': 'Grand Wizard', 'right': None,
                           'down': None, 'left': None}  # The enemy room
    }

    introduction()
    inventory = []
    player_health = 100
    wizard_health = 100
    current_room = 'Sanctuary'
    print(f"\nYou have arrived at the castle. You are in {current_room}.")
    print("You don't have any items yet.")

    # while loop to handle the game
    while True:
        # calls the player command function
        current_room = gameplay(current_room, rooms, inventory, player_health, wizard_health)

        # calls the display inventory function
        display_inventory(inventory)


if __name__ == '__main__':
    main()
