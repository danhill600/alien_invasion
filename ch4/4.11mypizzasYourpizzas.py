pizzas = [ 'green pepper', 'mushroom', 'pineapple' ]

friends_pizzas = pizzas[:]

friends_pizzas.append('artichokes')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for i in friends_pizzas:
    print(i)
