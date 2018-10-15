#9-1. Restaurant: Make a class called Restaurant . The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type .
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indi-
#cating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attri-
#butes individually, and then call both methods.

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

my_restaurant = Restaurant("zorba's", "greek")


print(my_restaurant.name.title() + " serves " + my_restaurant.cuisine.title()
      + " food.")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

second_restaurant = Restaurant("spaghetti shop", "italian")
third_restaurant = Restaurant("maize", "mexican")

second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()
