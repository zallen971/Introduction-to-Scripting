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
    print("\nThe Wizard's Will")
    print("The object is to collect 7 power source items to beat the grand wizard")
    print("Movement Commands: 'up', 'down', 'right', 'left', 'status' to "
          "see your current status, and 'exit' to quit the game")
    print("To add the power source item to inventory: p")
    print("________________________________________________________________\n")

    with open('./backstory.txt', 'r', encoding='utf-8') as file:  # calls the backstory text file
        backstory_content = file.read()

    print(backstory_content.rstrip())


# Gameplay: movement command , current/new room, inventory, grand wizard check
def gameplay(current_room, rooms, inventory, player_health, wizard_health):
    movement_command = input("What is your movement command: ")
    print()
    new_room = ''
    # if the player enters 'pick up item' it adds item to inventory and deletes it from the current room
    if movement_command == 'p':
        if 'item' in rooms[current_room]:
            item_name = rooms[current_room]["item"]  # gets the item in the room
            inventory.append(item_name)  # adds the item to the inventory list if the player enters p
            print('----------------------------------------------------------------')
            print(f"Way to go, you picked up the {item_name}. That's sure to come in handy!\n")
            del rooms[current_room]['item']  # deletes the item from the room so it doesn't keep notifying player
            if len(inventory) == 7:
                print("You have collected all 7 items!\n")
        else:
            print("No item in this room, you can tell.")
        return current_room

    # Movement commands for the player, also handles the exit and location, and invalid command
    if movement_command in rooms[current_room]:
        new_room = rooms[current_room][movement_command]

        # Check if new room is None
        if new_room is None:  # lets the player know there is no room that way
            print("There's no room in that direction.")
            return current_room
    elif movement_command == 'exit':  # print exit statement and close the game
        print('It would seem fate had other plans and you decide to not reclaim the castle'
              ' and confront the Grand Wizard!')
        print('Exiting the game...')
        exit()  # exit the game
    elif movement_command == 'status':  # if the player enters status it will call the show_status function
        show_status(current_room, rooms)
        return current_room
    else:
        print("Invalid movement command, must enter: up, down, right, left, p, location, exit")  # invalid command
        return current_room

    # lets the player know they moved to a new room
    if new_room:
        print('--------------------------------')
        print(f"You decide it's time to move to another room....")
        print(f'You move from {current_room} to {new_room}')
        current_room = new_room

        # prints a description of the room only if the room has one
        if new_room and new_room in rooms and 'description' in rooms[new_room]:
            description = rooms[new_room]['description']
            if description.strip():  # only print description if the room has one
                print(f"\n{rooms[new_room]['description']}\n")

        show_status(current_room, rooms)

        '''lets the player know that if there is an item in the room 
        they entered or not or if the grand wizard is in there'''
        if 'enemy' in rooms[
            new_room]:  # if the room has the grand wizard and the player has 7 items call battle function
            print("The Grand Wizard is in this room!")
            if len(inventory) == 7:
                print("You are ready to battle the Grand Wizard!\n")
                if battle_sequence(player_health, wizard_health):
                    exit()
            elif len(inventory) < 7:  # if the player doesn't have all 7 items, immediate defeat
                print("You don't have the power and the Grand Wizard one shot you!")
                print("Game Over!!")
                exit()

        return new_room


# function to display the inventory for the player and joins the items together to display
def display_inventory(inventory):
    if inventory:  # joins items together in the inventory and displays them for the player
        print("Your inventory: ", ", ".join(inventory))
    else:
        print("You don't have any items yet.\n")


# function to show the status including current room, directions and items
def show_status(current_room, rooms):
    # display the current room
    print(f'\nYou are currently in: {current_room}')

    # check for items in the current room and display them
    if 'item' in rooms[current_room]:
        print(
            f'\nYou feel the aura shift and see that there is the {rooms[current_room]["item"]} in here, you should '
            f'pick it up!')  # inform player there is an item in the room
        print('Enter p to pick the item up.\n')  # tell player the command to pick item up

    # display the valid movement directions
    directions = [direction for direction in ['up', 'down', 'left', 'right', ] if rooms[current_room].get(direction)]
    if directions:
        print(f'You can move: {", ".join(directions)}')  # tells player the valid movements that are available from room
    else:
        print('There are no valid directions you can move.')


# battle sequence function
def battle_sequence(player_health, wizard_health):
    # while both the player and wizard health are greater than 0 loop
    while player_health > 0 and wizard_health > 0:
        player_attack = random.randint(5, 30)  # gets a random attack power number between 5-30
        wizard_attack = random.randint(0, 20)  # gets a random attack power number between 0-20

        print(f"\nYou attack the Grand Wizard for {player_attack} damage")
        # sets it so the wizard health doesn't go into negative numbers
        wizard_health = max(wizard_health - player_attack, 0)
        print(f"The wizard has {wizard_health} health points left!\n")

        if wizard_health == 0:  # if wizard health reaches 0 then let the player know they won and exit game
            print("Congratulations, you have defeated the Grand Wizard and won the game!"
                  " Your will is strong and nobody can compare!")
            print("Reclaim the castle and bring wisdom, stability, and peace back into the lands!")
            return True

        print(f"The Grand Wizard attacked you for {wizard_attack} damage")
        # sets it so the player health doesn't go into the negative numbers
        player_health = max(player_health - wizard_attack, 0)
        print(f"You have {player_health} health points left!")

        if player_health == 0:  # if player health reaches 0 then let the player know they lost and exit game
            print("You were not strong enough to beat the Grand Wizard!")
            exit()


# dictionary to link each room and item. Crystal Cavern contains the Grand Wizard as well
def main():
    # Defines the rooms dictionary
    rooms = {
        'Sanctuary': {'up': 'The Whispering Gallery',
                      'right': 'Citadel',
                      'down': 'The Moonlit Garden',
                      'left': 'The Emerald Labyrinth'},  # Main entrance room

        'The Whispering Gallery': {'down': 'Sanctuary',
                                   'up': None,
                                   'right': None,
                                   'left': None,
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

        'Tower': {'left': 'Citadel',
                  'down': 'The Keep',
                  'item': 'Staff of Ancients',
                  'up': None,
                  'right': None,
                  'description': 'A place of solitude and mystery.It feels like a place of strength and isolation.'
                  },  # Staff of Ancients

        'The Keep': {'up': 'Tower',
                     'down': 'Crystal Cavern',
                     'item': 'Heart of a Dragon',
                     'right': None,
                     'left': None,
                     'description': 'crumbling furniture and structure, a place that once stood for the strength,'
                                    ' protection, and resilience of its people.'
                     },  # Heart of a Dragon

        'The Emerald Labyrinth': {'right': 'Sanctuary',
                                  'down': 'Shadowed Hall',
                                  'item': 'Orb of Elements',
                                  'up': 'The Archmage Sanctum',
                                  'left': None,
                                  'description': 'Emerald crystals shimmering, there are so many locked doors in here.'
                                  },  # Orb of Elements

        'Shadowed Hall': {'up': 'The Emerald Labyrinth',
                          'item': 'Amulet of Protection',
                          'right': None,
                          'left': None,
                          'down': None,
                          'description': 'Dark and cold hall seemingly stretched endlessly,'
                                         ' little light coming from the torches adorned on the walls.'},
        # Amulet of Protection

        'The Forgotten Chamber': {'up': 'The Moonlit Garden',
                                  'item': 'Soul Reaver Sword',
                                  'right': None,
                                  'left': None,
                                  'down': None,
                                  'description': 'The room has been long forgotten, shrouded in darkness.'
                                  },  # Soul Reaver Sword

        'The Archmage Sanctum': {'down': 'The Emerald Labyrinth', 'up': None,
                                 'left': None, 'right': None,
                                 'description': 'Ancient tomes sprawled on a desk, the smell of incense overtaking the air.'
                                 },  # empty room

        'Crystal Cavern': {'up': 'The Keep',
                           'enemy': 'Grand Wizard',
                           'right': None,
                           'down': None,
                           'left': None,
                           'description': ''}  # The enemy room - Grand Wizard
    }

    introduction()
    inventory = []
    player_health = 100
    wizard_health = 100
    current_room = 'Sanctuary'
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    print("After traveling many of fortnights, you finally start to see a building off into the distance. Although it's shrouded in darkness, you know for certain "
          "that it is the castle you are looking for")
    print("You are finally at the front of the castle, staring at the entrance! As you push open the front doors, you are greeted with lanters lighting "
          "the room. You look up and see a sign hanging, one simple word which you believe to be the name of the current room you're in; "
           f"{current_room}. Looking around, you decide which way should you go.....\n")
    print("You don't have any items yet.")

    # while loop to handle the game
    while True:
        # calls the player command function
        current_room = gameplay(current_room, rooms, inventory, player_health, wizard_health)

        # calls the display inventory function
        display_inventory(inventory)


if __name__ == '__main__':
    main()
