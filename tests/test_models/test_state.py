#!/usr/bin/python3
"""
unittests for module state
"""
import unittest
import datetime
from models.state import State


class TestState(unittest.TestCase):
    """ tests the class State, instances and methods """

    s = State()

    def test_classexists(self):
        """ tests whether the class exits """
        self.assertEqual(str(type(self.s)), "<class 'models.state.State'>")

    def test_stateinehritance(self):
        """ tests whether State is a sublcass of BaseModel """
        self.assertIsInstance(self.s, State)

    def test_hasattributes(self):
        """ tests whether all attributes exists """
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        """ tests whether attribute type is correct """
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
