#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
#ule. Make a separate file that imports Restaurant . Make a Restaurant instance,
#and call one of Restaurant ’s methods to show that the import statement is work-
#ing properly

from restaurant_module import Restaurant

myrestaurant = Restaurant("zorba's", "greek")

myrestaurant.describe_restaurant()
