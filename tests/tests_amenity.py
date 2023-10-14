#!/usr/bin/python3
"""this module is for amenity"""
import unittest
from models.amenity import Amenity

class AmenityTest(unittest.TestCase):
    """this class is for testing the amenity"""
    def test_attribute_type(self):
        """test the class here"""
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

