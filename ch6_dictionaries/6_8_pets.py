peanut = {
    'animal':'dog',
    'owner':['sarah','billy'],
}
scarlet = {
    'animal':'cat',
    'owner':['dan','mariam'],
}
glenn = {
    'animal':'cat',
    'owner':['sidrah']
}
huxley = {
    'animal':'dog',
    'owner':['mel'],
}
jack = {
    'animal':'dog',
    'owner':['kenny'],
}
melon = {
    'animal':'cat',
    'owner':['sam','rob'],
}
roo = {
    'animal':'dog',
    'owner':['sam','rob'],
}

pets = [peanut, scarlet, glenn, huxley, jack, melon, roo]
for pet in pets:
    if len(pet['owner']) == 1:
        print(str(pet['owner'][0]).title() + " has a " + pet['animal'])
    else:
        print(pet['owner'][0].title() + " and " + pet['owner'][1].title() +
              " have a " + pet['animal'])
