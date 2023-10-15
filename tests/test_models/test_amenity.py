#!/usr/bin/python3
"""
this module is for amenity
"""
import unittest
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """
    this class is for testing the amenity code
    """
    def test_attribute_type(self):
        """
        test the class here via the def
        """
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

    def test_inheritance(self):
        """
        this checks if Amenity does inherits from BaseModel.
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance_exist(self):
        """
        this functions checks if the amenity object exists.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == '__main__':
    unittest.main()
