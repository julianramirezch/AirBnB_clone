#!/usr/bin/python3
"""Module Test Case for FileStorage"""
import unittest
from datetime import datetime
import re
import os
import pep8
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """FileStorage Test Class"""
    @classmethod
    def setUpClass(cls):
        cls.p1 = Place()
        cls.p1.city_id = "Velez"
        cls.p1.state_id = "Santander"
        cls.p1.number_rooms = 7
        cls.p1.description = "Bocadillo City"

    @classmethod
    def tearDownClass(cls):
        del cls.p1

    def tearDown(self):
        """TearDown for each method in TestFileStorage class"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_pep8(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_fs_instance(self):
        """Test save and reload """
        b1 = BaseModel()
        models.storage.save()
        self.assertEqual(os.path.exists('file.json'), True)

        models.storage.reload()

    def test_errors(self):
        """Test errors"""
        b1 = BaseModel()
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_path

        with self.assertRaises(TypeError):
            models.storage.new()
            models.storage.new(self, b1)
            models.save(b1)
            models.reload(b1)
            models.all(b1)


if __name__ == '__main__':
    unittest.main()
