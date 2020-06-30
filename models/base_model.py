#!/usr/bin/python3
"""Module: BaseModel."""

import uuid
from datetime import datetime
import models
import json


class BaseModel:
    """Class BaseModel."""

    def __init__(self, *arg, **kwargs):
        """Do constructor for instances."""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Str method."""    
        name = type(self).__name__
        return ('[{}] ({}) {}'.format(name, self.id, self.__dict__))

    def save(self):
        """Update instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Create dict containing all keys/values of __dict__ of ins."""
        c_dic = dict(self.__dict__)
        c_dic['__class__'] = type(self).__name__
        c_dic['created_at'] = self.created_at.isoformat()
        c_dic['updated_at'] = self.updated_at.isoformat()
        return c_dic
