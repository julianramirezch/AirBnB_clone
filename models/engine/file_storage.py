#!/usr/python3
""" Module: Storage """

import json
from models.base_model import BaseModel
from models.user import User
# from models.amenity import Amenity
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State


class FileStorage:
    """ FileStorage Class """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        filename = FileStorage.__file_path
        serializes = {}
        for key, value in FileStorage.__objects.items():
            serializes[key] = value.to_dict()
        with open(filename, 'w', encoding='utf-8') as new_dict:
            json.dump(serializes, new_dict)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file """
        filename = FileStorage.__file_path
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reload_dict = json.load(f)
            for key, value in reload_dict.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
