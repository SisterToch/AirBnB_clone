#!/usr/bin/python3
"""this is a test model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """the main class for the test model"""

    def test_id_is_string(self):
        """this tests if the id is a string as
        we are supposed to make it one"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_created_at_is_datetime(self):
        """this test is to check the time allocated
        for created at"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """to test the updated at, if it follows the
        specified standard"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """checks for the saved updatess given"""
        my_model = BaseModel()
        previous_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(previous_updated_at, my_model.updated_at)

    def test_to_dict_contains_correct_keys(self):
        """does the todict provide the accurate keys?"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, my_model_dict)

    def test_to_dict_datetime_format(self):
        """this test tests the time format of base"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(
            datetime.strptime(my_model_dict['created_at'], date_format).isoformat(),
            my_model.created_at.isoformat()
           )
        self.assertEqual(
            datetime.strptime(my_model_dict['updated_at'], date_format).isoformat(),
            my_model.updated_at.isoformat()
        )

    def test_str_method_output(self):
        """here we are testing the string format
        of the basemodel"""
        my_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_output)

    def test_to_dict_returns(self):
        """we check if the to_dict feture works"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.to_dict(), dict)

    def test_xtra_attributes(self):
        """here we make the attributes for the instances"""
        my_model = BaseModel()
        my_model.name = "Tochukwu"
        my_model.number = 419
        my_model_dict = my_model.to_dict()
        self.assertIn('name', my_model_dict)
        self.assertIn('number', my_model_dict)
        self.assertEqual(my_model_dict['name'], "Tochukwu")
        self.assertEqual
