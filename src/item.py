class Item:
    def __init__(self, name, description):
        self.name = name  # instance variable
        self.description = description

    def on_take(self):
        """ 
        item is picked up
        """
        print("\n*************************************************")
        print(f"\nYou have picked up the {self.name}.")

    def on_drop(self):
        """
        item is dropped
        """
        print("\n*************************************************")
        print(f"\nYou have dropped the {self.name}.")

    def __getattr__(self, name):
        return None

    def __str__(self):
        return f"{self.name} - {self.description}"

    def __repr__(self):
        return f"Item({repr(self.name)}, {repr(self.description)})"


class Lamp(Item):
    def __init__(self, name, description, color):
        super().__init__(name, description)
        self.color = color

    def __str__(self):
        return f"{self.name} - {self.color}, {self.description}"

    def __repr__(self):
        return f"Lamp({repr(self.name)}, {repr(self.description)}, {repr(self.color)})"


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        return f"{self.name} - {self.value}, {self.description}"

    def __repr__(self):
        return f"Treasure({repr(self.name)}, {repr(self.description)}, {repr(self.value)})"


class Diamond(Treasure):
    def __init__(self, name, description, value, color):
        super().__init__(name, description, value)
        self.color = color

    def __str__(self):
        return f"{self.name} - {self.value}, {self.color}, {self.description}"

    def __repr__(self):
        return f"Diamond({repr(self.name)}, {repr(self.description)}, {repr(self.value)}, {repr(self.color)})"
