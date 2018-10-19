#9-1. Restaurant: Make a class called Restaurant . The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type .
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indi-
#cating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attri-
#butes individually, and then call both methods.

#9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
#Add an attribute called number_served with a default value of 0. Create an
#instance called restaurant from this class. Print the number of customers the
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number
#of customers that have been served. Call this method with a new number and
#print the value again.
#Add a method called increment_number_served() that lets you increment
#the number of customers who’ve been served. Call this method with any num-
#ber you like that could represent how many customers were served in, say, a
#day of business.

class Restaurant():
    """An attempt to model a restaurant"""
    def __init__(self, name, cuisine):
        """initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.numbers_served = 0

    def describe_restaurant(self):
        """tell the user about the restaurant"""
        print(self.name.title() + " serves " + self.cuisine + " food.")

    def open_restaurant(self):
        """open the restaurant for the day"""
        print(self.name.title() + " is now open")

    def increment_number_served(self, served_today):
        self.numbers_served = self.numbers_served + served_today

my_restaurant = Restaurant("zorba's", "greek")


print(my_restaurant.name.title() + " serves " + my_restaurant.cuisine.title()
      + " food.")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

second_restaurant = Restaurant("spaghetti shop", "italian")
third_restaurant = Restaurant("maize", "mexican")

second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()

restaurant = Restaurant('saucemans', 'american')
print(str(restaurant.numbers_served))
restaurant.numbers_served = 2
print(str(restaurant.numbers_served))

restaurant.increment_number_served(5)
print(str(restaurant.numbers_served))
