# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    name = ""
    description = ""

    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description

    def __repr__(self):
        r = f"(Room({repr(self.name)}, {repr(self.description)}))"
        return r
