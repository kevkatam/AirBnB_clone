#!/use/bin/python3
'''Module to test file storage'''

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''A class to test file storage'''

    def setUp(self):
        '''Set up object'''

        self.obj = FileStorage()

    @unittest.expectedFailure
    def test_all(self):
        '''Check all method'''

        self.assertEqual(self.obj.all(), FileStorage.objects)

    def test_attributes(self):
        '''Check class attributes'''

        self.assertFalse(hasattr(self.obj, '__objects'))
        self.assertFalse(hasattr(self.obj, '__file_path'))


if __name__ == '__main__':
    unittest.main()
