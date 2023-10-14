#!/usr/bin/python3
"""this module offers tests cases for city"""
import unittest
from models.city import City

class Test_City(unittest.TestCase):
    """class tests for city"""
    def test_attribute_types(self):
        """tests attribute"""
        city = City()
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(type(city.name), str)

