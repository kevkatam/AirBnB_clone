#!/usr/bin/python3
'''The base module'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''The base model'''

    def __init__(self, *args, **kwargs):
        '''Initialize objects'''

        if kwargs:
            for key, v in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    v = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''String representation'''
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        '''Update current time'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary'''
        dictionary = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                dictionary[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not v:
                    pass
                else:
                    dictionary[k] = v
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
