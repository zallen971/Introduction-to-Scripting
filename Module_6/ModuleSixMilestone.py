"""
Zachary Allen
IT-140: Introduction to Scripting
Module Six Milestone
"""


# introduction function for the player
def introduction():
    print('Movement commands: North, East, South, West, or exit to leave the game.')


# Movement function to handle the player moving through rooms
def gameplay(rooms, current_room):
    command = input('Enter your movement command: ').lower()
    print()
    new_room = current_room

    # if/elif/else statement to handle player navigation through rooms
    if command == 'north':
        new_room = rooms[current_room].get('North', current_room)
    elif command == 'east':
        new_room = rooms[current_room].get('East', current_room)
    elif command == 'south':
        new_room = rooms[current_room].get('South', current_room)
    elif command == 'west':
        new_room = rooms[current_room].get('West', current_room)
    elif command == 'exit':
        print('exiting...')
        exit()
    else:
        print('Invalid command. Must enter: North, East, South, West, exit')
        return current_room

    """
    If/else statement to inform the player they entered a new room
    or inform them if there is no room in the direction they are trying to go.
    """
    if new_room != current_room:
        print(f'You moved from {current_room} to {new_room}.')
        print(f"\nyou're currently in {new_room}")
    else:
        print('There is no room that way.')

    return new_room


# Main function, dictionary for the rooms
def main():
    # rooms dictionary
    rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

    game_running = True

    # call the introduction function
    introduction()
    # sets initial room to Great Hall
    current_room = 'Great Hall'
    print(f'You are currently in {current_room}')

    # while loop to handle the game
    while game_running:
        next_room = gameplay(rooms, current_room)
        if next_room is None:
            print("Thanks for playing!!")
            game_running = False
        else:
            current_room = next_room


if __name__ == '__main__':
    main()
