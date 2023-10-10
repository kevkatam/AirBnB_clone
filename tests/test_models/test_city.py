#!/usr/bin/python3
"""
unittests for the module city
"""
import unittest
from models.city import City


class TestCity(unittest.TasteCase):
    """ tests the class City """
    c = City

    def test_classexists(self):
        """ tests whether the class City exists """
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")

    def test_inheritance(self):
        """ tests whether the class City is a subclass of BaseModel """
        self.assertIsInstance(self.c, City)

    def test_hasattributes(self):
        """ test whether the class City has all attributes """
        self.assertTrue(hasattr(self.c, state_id))
        self.assertTrue(hasattr(self.c, name))

    def test_type(self):
        """ tests whether the type of the attribute is correct """
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.name, str)


if __name__ == '__main__':
    unittest.main()
