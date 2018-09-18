#8-6. City Names: Write a function called city_country() that takes in the name
#of a city and its country. The function should return a string formatted like this:
#    "Santiago, Chile"
#Call your function with at least three city-country pairs, and print the value

def city_state(city, state):
    pair = city.title() + "," + state.title()
    return pair

pair = city_state('chicago','illinois')
print(pair)
pair = city_state('syracuse','new york')
print(pair)
pair = city_state('denver','colorado')
print(pair)
