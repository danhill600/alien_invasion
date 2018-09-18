def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#the asterisk in the parameter name *toppings tellsPython to make an empty 
#tuple called toppings and pack whatever values it receives into this tuple.
