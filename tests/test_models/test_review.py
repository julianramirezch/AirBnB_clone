#!/usr/bin/python3
""" Review unit testing """
import unittest
import pep8
import json
from models.base_model import BaseModel
from models.review import Review


class TestReviewRequirements(unittest.TestCase):
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
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        path_file = 'tests/test_models/test_review.py'
        result = pep8style.check_files([path_file])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(Review.__doc__) >= 1)
