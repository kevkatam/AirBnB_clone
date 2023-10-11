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
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''String representation'''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Update current time'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary'''
        
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
