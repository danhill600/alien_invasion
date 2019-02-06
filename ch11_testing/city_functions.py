#Write a function that accepts two parameters: a city name and a country name. 
#The function should return a single string of the form City, Country such as
#Santiago, Chile.  Store the function in a module called city_functions.py
#
#Create a file called test_cities.py that tests the function you just wrote
#(remember that you need to import unittest and the function you want to test).
#Write a method called test_city_country() to verify that calling your function
#with values such as 'santiago' and 'chile' results in the correct string.  RUn
#test_cities.py, and make sure test_city_country() passes.

def get_formatted_city_country(city, country, population=''):
    """return a string such as 'Santiago, Chile - 5000000'"""
    if population:
        return city.title() + ', ' + country.title() + ' - population ' + population
    else:
        return city.title() + ', ' + country.title()

print("'q' to quit at any time dude")
while True:
    city = input("well what city are you talking about?:")
    if city == 'q':
        break
    country = input("well what country are you talking about?:")
    if country == 'q':
        break
    population = input("how many people live there?: ")
    if population == 'q':
        break
    if population:
        formatted_city_country = get_formatted_city_country(city, country, population)
        print("\tNeatly formatted city/country/pop: " + formatted_city_country + '.')
    else:
        formatted_city_country = get_formatted_city_country(city, country)
        print("\tNeatly formatted city/country: " + formatted_city_country + '.')
