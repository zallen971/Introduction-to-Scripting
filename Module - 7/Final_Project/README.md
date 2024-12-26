The Wizards Will Text-Based Adventure Game

Overview

This project involved creating a text-based aventure game in Python. The game requred the player to navigate through rooms, collect items, and avoid the villian to win. The objective is to collect all the items before entering the room with the villain.

Summary:

* Objective: Collect seven power source items scattered throughout the castle to defeat the Grand Wizard. These seven items give you the ability to challenge the Grand Wizard, without them it's an immediate defeat.

* Movement Commands:
* The player can use the following commands to navigate the castle:
  Up
  Down
  Left
  Right

* The player can use the following commands for other options:
  status - This shows the current status including location and items in the inventory
  exit - This will quit the game

Rooms:

The castle consists of interconnected rooms, each with unique descriptions and features. Some rooms contain items vital for success, while others are empty.
The Grand Wizard resides in the Crystal Caverns


Items:

The seven power source items include - 
1. Boots of the Flamewalker
2. Spell Book of the Dead
3. Staff of Ancients
4. Heart of a Dragon
5. Orb of Elements
6. Amulet of Protection
7. Soul Reaver Sword


Battle:

Upon encountering the Grand Wizard with all items, a battle ensues. Both player and wizard have health points with attacks being randomized. The player wins when the wizard's health reaches zero and the wizard wins when the player's health reaches zero

----------------------------------------------------------------------------------------------------------------------------

Instructions:

Game Start - 
1. Launch the game by running the Python script.
2. Read the backstory displayed at the beginning of the game.
3. Begin your journey in the Sanctuary, the castle's entrance.


Navigation -
- up, down, left, right: Move to adjacent rooms.
- p: Pick up items in the current room.
- status: Display your current room, inventory, and possible directions.
- exit: Quit the game.


Inventory Management -
- Items found in rooms can be collected by typing p.
- View your inventory any time to track collected items.

Winning the Game -
- Ensure all seven items are collected before confronting the Grand Wizard
- If you meet the Grand Wizard without all items, you lose immediately

----------------------------------------------------------------------------------------------------------------------------

Game Map:

Rooms Overview -
1. Sanctuary: Starting point; connects to several key locations
2. The Whispering Gallery: Contains the Boots of the Flamewalker
3. Citadel: Contains the Spell Book of the Dead
4. The Moonlit Garden: Empty room
5. Tower: Contains the Staff of Ancients
6. The Keep: Contains the Heart of a Dragon
7. The Emerald Labyrinth: Contains the Orb of Elements
8. Shadowed Hall: Contains the Amulet of Protection
9. The Forgotten Chamber: Contains the Soul Reaver Sword
10. The Archmage Sanctum: Empty room
11. Crystal Vavern: The Grand Wizard's Lair

----------------------------------------------------------------------------------------------------------------------------

Debugging and Testing:

Debugging Tips -
- Use the provided speedrun directions to quickly test the game's winning path
- Test various scenarios such as:
    - Moving to rooms without items
    - Picking up items in different orders
    - Entering invalid commands

Testing Scenarios -
- Winning: Ensure the player can defeat the Grand Wizard when all items are collected
- Losing: Verify the game ends if the player enters the Grand Wizard's room prematurely
- Error Handling: Check that invalid commands are handled gracefully

----------------------------------------------------------------------------------------------------------------------------

Conclusion:

The Wizard's Will combines storytelling, strategy, and Python programming to create an engaging text-based adventure. Debug, test, and enjoy reclaiming the castle and restoring peace to the lands!
