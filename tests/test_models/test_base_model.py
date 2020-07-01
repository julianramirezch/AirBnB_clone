#!/usr/bin/python3
''' Base unittesting '''

import unittest
import pep8
import json
from models import base_model
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBasedocu(unittest.TestCase):
    ''' test Base Documentation '''

    def test_pep8(self):
        """ Test that models/base_model.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix Your PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(r.total_errors, 0, "Fix Your PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(base_model.__doc__) >= 1)


class TestBaseFunctions(unittest.TestCase):
    """ Test base class """

    @classmethod
    def setUpClass(cls):
        '''
        is called with the class as the only argument
        and must be decorated as a classmethod():
        '''
        pass

    @classmethod
    def tearDown(cls):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_init(self):
        """check instance"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_uniq_id(self):
        ''' check for id creation '''
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertFalse(b1.id == b2.id)

    def test_typos(self):
        ''' check for id creation '''
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.name, str)
        self.assertIsInstance(b1.my_number, int)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertIsInstance(b1.__class__(), BaseModel)

    def test_kwargs_constructor(self):
        ''' Create object passing Kwargs '''
        my_dict = {
                    'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                    'created_at': '2025-06-28T14:00:00.000001',
                    '__class__': 'BaseModel',
                    'updated_at': '2030-06-28T14:00:00.000001',
                    'score': 100
                }
        obj = BaseModel(**my_dict)
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(obj.__class__ == 'BaseModel')
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'score'))
        self.assertEqual(obj.id, 'cc9909cf-a909-9b90-9999-999fd99ca9a9')
        self.assertEqual(
            obj.created_at.isoformat(),
            '2025-06-28T14:00:00.000001')
        self.assertEqual(
            obj.updated_at.isoformat(),
            '2030-06-28T14:00:00.000001')
        self.assertEqual(obj.score, 100)

    def test_attr_nan(self):
        """NaN attribute."""
        obj = BaseModel(float("nan"))
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_attr_inf(self):
        """Inf attribute."""
        obj = BaseModel(float("inf"))
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_str_method(self):
        ''' Test str method '''
        obj = BaseModel()
        out = "[{}] ({}) {}\n".format(type(obj).__name__, obj.id, obj.__dict__)

        def test_str(self):
            self.assert_stdout(out)

    def test_save_method(self):
        ''' Test save method '''
        obj = BaseModel()
        updated = obj.updated_at
        obj.save()
        self.assertTrue(updated != obj.updated_at)

    def test_before_todict(self):
        """Tests the instance before using the todict conversion"""
        b1 = BaseModel()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """Tests instances after using to_dict conversion"""
        my_model = BaseModel()
        new_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(test_dict['__class__'], "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_file_storage(self):
        """check save_to_file"""
        obj = BaseModel()
        obj.save()
        exists = os.path.exists('file.json')
        self.assertTrue(exists, True)
