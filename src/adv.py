from room import Room
from player import Player
from item import Item
from item import Lamp
from item import Treasure
from item import Diamond

# Declare all the rooms
# It tells you how to create the room class with attributes

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", []),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Lamp("torch", "It's a torch. The fire sways in a breeze.", "red")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("key", "An ancient skeleton key. It looks like it'll fit in any door.")]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("knife", "A knife you've almost stepped on.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Diamond("diamond", "This diamond is so bright it almost hurts your eyes.", "$20,000", "platinum")]),
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
player_name = input("What is your name?: ")
p = Player(player_name, [])

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

# Create a player
# Let player input their name
print(f"\nReady, {p.name}? Let's start!")

done = False

# Create basic REPL loop


def choose_room(new_room):
    if new_room.name == "Outside Cave Entrance":
        p.set_room("outside")
    elif new_room.name == "Foyer":
        p.set_room("foyer")
    elif new_room.name == "Grand Overlook":
        p.set_room("overlook")
    elif new_room.name == "Narrow Passage":
        p.set_room("narrow")
    elif new_room.name == "Treasure Chamber":
        p.set_room("treasure")
    else:
        print("\nYou must select a valid direction.")


def build_initial_comment():
    s = "You can move"
    if room[p.current_room].n_to is not None:
        s += " n,"
    if room[p.current_room].s_to is not None:
        s += " s,"
    if room[p.current_room].w_to is not None:
        s += " w,"
    if room[p.current_room].e_to is not None:
        s += " e,"
    if len(p.item_list) > 0:
        s += " drop [item],"
    if len(room[p.current_room].item_list) > 0:
        s += " get [item],"
    s += " inventory/i, or (exit): "
    return s


while done is False:
    print("\n**********************************************")
    print(f"\nYou are currently in {room[p.current_room].name}.")
    print(room[p.current_room].description)

    if len(room[p.current_room].item_list) > 0:
        print("\nItems in room:")
        room[p.current_room].print_items()

    try:
        selection = input("\n" + build_initial_comment()
                          ).strip().lower().split(" ")

        new_room = None

        if selection[0].lower() == "exit":
            print("\nIt's dangerous out there... take this! (hands you the torch)\n")
            done = Treasure
            continue
        elif selection[0] == "i" or selection[0] == "inventory":
            if len(p.item_list) > 0:
                print("\n**********************************************")
                print(f"\nItems in inventory...")
                for item in p.item_list:
                    print(item)
            else:
                print("\n**********************************************")
                print(f"\nThere are no items in your inventory!")
        elif selection[0].lower() == "n":
            new_room = room[p.current_room].n_to
            choose_room(new_room)

        elif selection[0].lower() == "s":
            new_room = room[p.current_room].s_to
            choose_room(new_room)

        elif selection[0].lower() == "e":
            new_room = room[p.current_room].e_to
            choose_room(new_room)

        elif selection[0].lower() == "w":
            new_room = room[p.current_room].w_to
            choose_room(new_room)
        elif selection[0] == "take" or selection[0] == "get":
            item_moved = False
            for item in room[p.current_room].item_list:
                if item.name.lower() == selection[1]:
                    p.add_item(item)
                    room[p.current_room].remove_item(item)
                    item_moved = True
                    item.on_take()
            if not item_moved:
                print("\n**********************************************")
                print(f"\nThere's no item by that name.")
                continue
        elif selection[0] == "drop" or selection[0] == "leave":
            item_moved = False
            for item in p.item_list:
                if item.name.lower() == selection[1]:
                    p.remove_item(item)
                    room[p.current_room].add_item(item)
                    item_moved = True
                    item.on_drop()
                if item.name == "torch":
                    print("\n**********************************************")
                    print(f"\nYou shouldn't leave your torch here!")
            if not item_moved:
                print("\n**********************************************")
                print(f"\nThat item is not in your inventory!")
                continue

    except:
        print("\n**********************************************")
        print(f"\nThat item is not in your inventory!")
        continue
