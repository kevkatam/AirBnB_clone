#!/usr/bin/python3
"""
unittest for module amenity
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """ tests instances and methods of the class Amenity """
    a = Amenity()

    def test_classexists(self):
        """ tests if the class amenity exists """
        self.assertEqual(str(type(self.a)), "<class 'models.amenity.Amenity'>")

    def test_inheritance(self):
        """ tests whether the class Aminity is a subclass of class BaseModel
        """
        self.assertIsInstance(self.a, Amenity)

    def test_hasattributes(self):
        """ tests whether the class Amenity has all attributes """
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_type(self):
        """ tests whether the type of the attribute is correct """
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
