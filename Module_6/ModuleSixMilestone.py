"""
Zachary Allen
IT-140: Introduction to Scripting
Module Six Milestone
"""


# introduction function for the player
def introduction():
    print('Movement commands: North, East, South, West, or Exit')

# Movement function to handle the player moving through rooms
def gameplay(rooms, current_room):
    command = input('Enter your movement command: ')
    new_room = ''

    if command == 'North':
        new_room = rooms[current_room]["North"]
    elif command == 'East':
        new_room = rooms[current_room]["East"]
    elif command == 'South':
        new_room = rooms[current_room]["South"]
    elif command == 'West':
        new_room = rooms[current_room]["West"]
    elif command == 'exit':
        exit()
    else:
        print('Invalid command. Must enter: North, East, South, West, exit')


# Main function, dictionary for the rooms
def main():
    # rooms dictionary
    rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

    # call the introduction function
    introduction()
    # sets initial room to Great Hall
    current_room = 'Great Hall'
    print(f'You are currently in {current_room}')

    # while loop to handle the game
    while True:
        # calls the movement command function
        current_room = gameplay(current_room, rooms)


if __name__ == '__main__':
    main()
