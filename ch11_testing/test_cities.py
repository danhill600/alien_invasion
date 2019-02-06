import unittest
from city_functions import get_formatted_city_country


class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Do combos like 'Santiago, Chile' work?"""
        formatted_city_country = get_formatted_city_country('santiago', 'chili')
        self.assertEqual(formatted_city_country, 'Santiago, Chili')
    def test_city_country_population(self):
        """Do combos like 'Chicago, Illinois - population 6000000' work?"""
        formatted_city_country = get_formatted_city_country('chicago', 'illinois', '6000000')
        self.assertEqual(formatted_city_country , 'Chicago, Illinois - population 6000000')
unittest.main()
