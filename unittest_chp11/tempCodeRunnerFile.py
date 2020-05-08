import unittest

from city_functions import city_country


class TestCities(unittest.TestCase):
    def test_city_country(self):
        citycountry = city_country('Banjul', 'Gambia')
        self.assertEqual(citycountry, 'Banjul, Gambisa')

if __name__ == '__main__':
    unittest.main()
        
