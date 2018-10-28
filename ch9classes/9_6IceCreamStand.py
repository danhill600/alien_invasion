#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
#a class called IceCreamStand that inherits from the Restaurant class you wrote
#in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
#the class will work; just pick the one you like better. Add an attribute called
#flavors that stores a list of ice cream flavors. Write a method that displays
#these flavors. Create an instance of IceCreamStand , and call this method.

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

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        self.flavors = [ 'vanilla',
            'chocolate',
            'ice-beam',
            ]

    def display_flavors(self):
        print(self.flavors)

jennys=IceCreamStand("Jenny's","halftrashy")

jennys.display_flavors()
