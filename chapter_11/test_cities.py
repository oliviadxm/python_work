import unittest
from city_functions import format_city


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_city = format_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_city = format_city('santiago', 'chile', '5000000')
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')


if __name__ == '__main__':
    unittest.main()