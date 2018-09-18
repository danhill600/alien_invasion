#8-12. Sandwiches: Write a function that accepts a list of items a person wants
#on a sandwich. The function should have one parameter that collects as many
#items as the function call provides, and it should print a summary of the sand-
#wich that is being ordered. Call the function three times, using a different num-
#ber of arguments each times.

def sandwiches(*ingredients):
    """prints the full list of ingredients for a sandwich"""
    print("Your sandwich includes:")
    for ingredient in ingredients:
        print("-" + ingredient)


sandwiches('turkey','peanut butter','toothpaste')
sandwiches('tomatillos','grass','a different sandwich')
sandwiches('apples','birdseed','a perfect reverse birth')
