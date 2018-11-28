#9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
#used a standard dictionary to represent a glossary. Rewrite the program using
#the OrderedDict class and make sure the order of the output matches the order
#in which key-value pairs were added to the dictionary.

from collections import OrderedDict

words = OrderedDict()

words['schprogram'] = 'algorithm'
words['schvariabl'] = 'schminprut'
words['schmist'] = 'grouping'
words['schprint'] = 'output'
words['conditional'] = 'operator'


for i,j in words.items():
    print(i + ":" + j + "\n")
