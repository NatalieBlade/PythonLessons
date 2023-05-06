import unittest
from city_functions import city_country

class CityTastCase(unittest.TestCase):

    def test_city_country(self):
        format_city = city_country("Santiago", "Chile")
        self.assertEqual(format_city, "Santiago, Chile")

    def test_city_country_inhabitants(self):
        format_city = city_country("Santiago", "Chile", "451000")
        self.assertEqual(format_city, "Santiago, Chile, 451000")

if __name__ == "__name__":
    unittest.main()