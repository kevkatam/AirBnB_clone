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
<<<<<<< HEAD
                    value = datetime.fromisoformat(value)
=======
                    value = datetime.strptime(kwargs[key],
                                              "%Y-%m-%dT%H:%M:%S.%f")
>>>>>>> 34baaa4ff68929ba0173ed1467bd180d6fecc602

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
<<<<<<< HEAD

        dictionary = self.__dict__
=======
        dictionary = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                dictionary[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not v:
                    pass
                else:
                    dictionary[k] = v
>>>>>>> 34baaa4ff68929ba0173ed1467bd180d6fecc602
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
