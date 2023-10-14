#!/usr/bin/python3
'''Test Base Model'''

import unittest
import datetime
from models.base_model import BaseModel
from models.engine .file_storage import FileStorage
import os
from models import storage


class TestBaseModel(unittest.TestCase):
    '''Class to test base model'''

    model = BaseModel()

    def test_basemodel(self):
        """ tests the values of attributes of an instance of basemodel """
        self.model.name = "Kevin"
        self.model.number = 98
        self.model.save()
        modeljson = self.model.to_dict()

        self.assertEqual(self.model.name, modeljson['name'])
        self.assertEqual(self.model.number, modeljson['number'])
        self.assertEqual('BaseModel', modeljson['__class__'])
        self.assertEqual(self.model.id, modeljson['id'])

    def test_save(self):
        """ tests the save method """
        self.model.first_name = "alx"
        self.model.save()

        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

        dict_1 = self.model.to_dict()

        self.model.first_name = "school"
        self.model.save()

        dict_2 = self.model.to_dict()

        self.assertEqual(dict_1['created_at'], dict_2['created_at'])
        self.assertNotEqual(dict_1['updated_at'], dict_2['updated_at'])


if __name__ == '__main__':
    unittest.main()
