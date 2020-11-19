# Bren007pie July 8, 2020 NEVADA Outline of game classes

class Entity():
    def __init__(self, ID, name, description, inventory):
        self.entityID = ID
        self.name = name
        self.description = description
        self.inventory = inventory

    def get_ID(self):
        return(self.entityID)

    def get_name(self):
        return(self.name)

    def set_name(self, new_name):
        self.name = new_name

    def get_description(self):
        return(self.description)

    def set_description(self,new_description):
        self.description = new_description

    def get_inventory(self):
        return(self.inventory)

    def set_inventory(self,new_inventory):
        self.inventory = new_inventory

    def add_to_inventory(self,addiition ):
        self.inventory.append(addiition)

    def remove_from_inventory(self,removal):
        self.inventory.remove(removal)

    def is_in_inventory(self,search):
        return(self.inventory.__contains__(search))

    def update(self):  # this is a template for polymorphism from inheritted classes
        # https: // gameprogrammingpatterns.com / update - method.html
        # The game loop maintains a collection of objects, but it doesn’t know their concrete types.
        # All it knows is that they can be updated.
        # This separates each object’s behavior both from the game loop and from the other objects.
        pass

