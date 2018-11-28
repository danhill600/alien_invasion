#9-14. Dice: The module random contains functions that generate random num-
#bers in a variety of ways. The function randint() returns an integer in the
#range you provide. The following code returns a number between 1 and 6:
#
#    from random import randint
#    x = randint(1, 6)
#
#Make a class Die with one attribute called sides , which has a default
#value of 6. Write a method called roll_die() that prints a random number
#between 1 and the number of sides the die has. Make a 6-sided die and roll
#it 10 times.
from random import randint

class Dice():
    """A simple attempt to represent a die"""

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)
my_die = Dice()
#my_die.roll_die()

for i in range(1,10):
    my_die.roll_die()
