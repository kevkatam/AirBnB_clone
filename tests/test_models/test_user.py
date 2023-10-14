#!/usr/bin/python3
"""
unittests fro module user.py
"""
import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """ tests methods and instances from User class """
    u = User()

    def test_classexists(self):
        """ tests if the class exists """
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_inheritance(self):
        """ tests if class User inherits or is subclass of class BaseModel """
        self.assertIsInstance(self.u, User)

    def test_has_attributes(self):
        """ tests if all attributes exit """
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_types(self):
        """ test if attribute type is correct """
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.password, str)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.created_at, datetime.datetime)
        self.assertIsInstance(self.u.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
