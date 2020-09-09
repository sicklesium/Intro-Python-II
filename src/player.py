# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    name = ""
    current_room = ""

    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room

    def __repr__(self):
        r = f"(Player({repr(self.name)}, {repr(self.current_room)}))"
        return r
