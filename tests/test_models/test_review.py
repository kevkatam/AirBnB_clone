#!/usr/bin/python3
"""
unittest for the module review
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ tests for methods and instances in class Review """

    r = Review()

    def test_classexists(self):
        """ tests whether the class Review exists """
        self.assertEqual(str(type(self.r)), "<class 'models.review.Review'>")

    def test_inheritance(self):
        """ tests whether the class Review inherits class BaseModel """
        self.assertIsInstance(self.r, Review)

    def test_hasattributes(self):
        """ tests whther the class Review has all attributes """
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))

    def test_types(self):
        """ tests whether the attributes have correct types """
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.created_at, datetime.datetime)
        self.assertIsInstance(self.r.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
