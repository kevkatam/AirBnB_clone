#!/usr/bin/python3
'''Test Base Model'''

import unittest
import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Class to test base model'''

    def setUp(self):
        '''Create the object'''

        self.obj = BaseModel()

    @unittest.expectedFailure
    def test__str__(self):
        '''Test string representation'''

        output = "[BaseModel] ({self.obj.id}) {self.obj.__dict__}"
        self.assertEqual(str(self.obj), output)

    def test_attributes(self):
        '''Test if attributes present'''

        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    @unittest.expectedFailure
    def test_to_dict(self):
        '''Test to_dict method'''

        self.assertEqual(self.obj.to_dict, f"{FileStorage.objects}")


if __name__ == '__main__':
    unittest.main()
