class Player:
    # Init player with name
    def __init__(self, name, item_list):
        """ 
        This is constructor function that creates all needed variables for instantiation of a new player
        """
        # Player also has attr current_room - every player needs to be in a room to start playing
        self.current_room = "outside"
        self.name = name
        self.item_list = item_list

    def set_room(self, current_room):
        """
        This method sets the new room for the player as they move throughout the game
        """
        self.current_room = current_room

    def add_item(self, item):
        """
        Adds in a new item to the player's inventory
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

    def __str__(self):
        """
        Replacement string method for the Player class
        """
        return f"Name: {self.name}, Room: {self.room}, Items: {self.item_list}."

    def __repr__(self):
        """
        REPR method for the Player class
        """
        return f"Player({repr(self.name)}, {repr(self.item_list)})"
