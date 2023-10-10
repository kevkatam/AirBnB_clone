#!/usr/bin/python3
"""
unittests fro module user.py
"""
import unittest
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
