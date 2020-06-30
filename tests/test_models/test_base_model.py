#!/usr/bin/python3
""" BaseModel unit testing """
import unittest
import pep8
import json
from models.base_model import BaseModel
from datetime import datetime
import uuid
import json


class TestBaseModelRequirements(unittest.TestCase):
    """ Tests base documentation """

    @classmethod
    def setUpClass(cls):
        '''
        is called with the class as the only argument
        and must be decorated as a classmethod():
        '''
        pass

    @classmethod
    def tearDownClass(cls):
        '''
        is called with the class as the only argument
        and must be decorated as a classmethod():
        '''
        pass

    def test_pep8(self):
        """ Test that models/base.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        # path_f = 'tests/test_models/test_base_model.py'
        result = pep8style.check_files(['tests/test_models/\
test_base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(BaseModel.__doc__) >= 1)
