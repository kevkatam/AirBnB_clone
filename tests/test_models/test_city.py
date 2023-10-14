#!/usr/bin/python3
"""
unittests for the module city
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """ tests the class City """
    c = City()

    def test_classexists(self):
        """ tests whether the class City exists """
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")

    def test_inheritance(self):
        """ tests whether the class City is a subclass of BaseModel """
        self.assertTrue(self.c, City)

    def test_hasattributes(self):
        """ test whether the class City has all attributes """
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))

    def test_type(self):
        """ tests whether the type of the attribute is correct """
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.created_at, datetime.datetime)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
