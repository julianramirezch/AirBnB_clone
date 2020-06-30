#!/usr/python3
""" Module: Storage """

import json
from models.base_model import BaseModel


class FileStorage:
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
            print('pre serialize key {}'.format(FileStorage.__objects[key]))
            print('\n\n')
            serializes[key] = value.to_dict()
            print('serializes key {}'.format(serializes[key]))
            print('\n\n')
        with open(filename, 'w', encoding='utf-8') as new_dict:
            json.dump(serializes, new_dict)
        print(new_dict)
        print('\n\n')

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file """
        filename = FileStorage.__file_path
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reload_dict = json.load(f)
            for key, value in reload_dict.items():
                print('key >>>{}'.format(key))
                print('\n\n')
                print('value >>>{}'.format(value))
                print('\n\n')
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except:
            pass

