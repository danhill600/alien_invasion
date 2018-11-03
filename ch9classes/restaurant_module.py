"""a module about restaurants"""
class Restaurant():
    """An attempt to model a restaurant"""
    def __init__(self, name, cuisine):
        """initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """tell the user about the restaurant"""
        print(self.name.title() + " serves " + self.cuisine + " food.")

    def open_restaurant(self):
        """open the restaurant for the day"""
        print(self.name.title() + " is now open")
