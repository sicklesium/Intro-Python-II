class Room:
    def __init__(self, name, description, item_list):
        # Name, description
        self.name = name
        self.description = description
        self.item_list = item_list

        # n_to, s_to, e_to, w_to - North, South, East, West - no need to def since it defaults to none - being explicit - we have these 4 attributes
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"\n{self.name}\n\n{self.description}"

    def get_name(self):
        return self.name

    # TODO - self is the room obj and going to set the direction of the player and the actual room obj.
    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def print_items(self):
        """
        Prints all items in the item_list
        """
        for item in self.item_list:
            print(item)
        print()

    def add_item(self, item):
        """
        Adds a new item to the Room's inventory when a player drops it
        """
        self.item_list.append(item)

    def remove_item(self, item):
        """
        Drops an item from the Room's inventory
        """
        new_item_list = []
        for i in self.item_list:
            if i.name is not item.name:
                new_item_list.append(i)
        self.item_list = new_item_list

    def __getattr__(self, name):
        """
        Defaults to None for any attribute not in the class currently
        """
        return None

    def __repr__(self):
        """
        REPR method for the Room class
        """
        return f"Room({repr(self.name)}, {repr(self.description)}, {repr(self.item_list)})"
