#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_id_is_string(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_created_at_is_datetime(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        my_model = BaseModel()
        previous_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(previous_updated_at, my_model.updated_at)

    def test_to_dict_contains_correct_keys(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, my_model_dict)

    def test_to_dict_datetime_format(self):
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
        my_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_output)

    def test_to_dict_returns_dict(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.to_dict(), dict)

    def test_extra_attributes(self):
        my_model = BaseModel()
        my_model.name = "Test"
        my_model.number = 123
        my_model_dict = my_model.to_dict()
        self.assertIn('name', my_model_dict)
        self.assertIn('number', my_model_dict)
        self.assertEqual(my_model_dict['name'], "Test")
        self.assertEqual
