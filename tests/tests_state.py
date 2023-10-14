#!/usr/bin/python3
"""this module explains the unitests"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """this is for the test cases"""
    def test_attribute_type(self):
        """class for state"""
        state = State()
        self.assertEqual(type(state.name), str)

