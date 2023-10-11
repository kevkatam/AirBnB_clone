#!/usr/bin/python3
'''File storage module'''


import json
import os.path

class FileStorage:
    '''Persistent file storage'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Return dictionary'''

        return FileStorage.__objects

    def new(self, obj):
        '''Set object'''

        class_name = type(obj).__name__
        o_id = str(obj.id)
        FileStorage.__objects['{class_name}.{o_id}'] = obj

    def save(self):
        '''Serialize to JSON'''

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        '''Deserialize from JSON'''

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        else:
            pass
