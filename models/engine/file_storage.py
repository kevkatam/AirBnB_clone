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
        k = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[k] = obj

    def save(self):
        '''Serialize to JSON'''
        d = {}
        for k, v in FileStorage.__objects.items():
            d[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(d, f)

    def reload(self):
        '''Deserialize from JSON'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        d = {'BaseModel': BaseModel, 'User': User, 'State': State,
             'City': City, 'Amenity': Amenity, 'Place': Place,
             'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for k, v in json.load(f).items():
                    self.new(d[v['__class__']](**v))
