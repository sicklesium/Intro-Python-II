from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Halcy", room["outside"])

# initial stuff
current = player.current_room

print(f"You are currently at {current.name}. {current.description}.\n")

# input prompt!

command = input("Enter a command (n, e, s, w, or q): ")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Start while loop, as long as q is not entered to quit, continue the loop
while command != 'q':
    # If a direction is entered use control flow to move player
    if (command in ['n', 'e', 's', 'w']):
        # If valid direction is entered, check for route existence
        dir_attr = f"{command}_to"
        if hasattr(current, dir_attr):
            # If route exists, update current room and room items and print
            current = getattr(current, dir_attr)
            print(
                f"You are currently at {current.name}. {current.description}.\n")
        # If route does not exist, print error message
        else:
            print(f"There is nothing in that direction.")
    # If a different command is entered let player know the command is not valid
    else:
        print(f"Please enter a valid command (n, e, s, w, or q).")
    # Re-prompt after each while loop
    command = input("Enter a command (n, e, s, w, or q): ")
# If q is entered, print farewell message
if (command == 'q'):
    print(f"It's dangerous out there...")
