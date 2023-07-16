#!/usr/bin/python3
"""
This is State class unittest module. This class tests State class.
"""
import unittest
import uuid
import datetime
from models.state import State


class TestState(unittest.TestCase):
    """
    Create object of State class for testing.
    """
    def setUp(self):
        self.mystate1 = State()
        self.mystate2 = State()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.mystate1, "name"))
        self.assertFalse(hasattr(self.mystate2, "place"))
        self.assertTrue(type(self.mystate1.name) is str)
        self.assertTrue(type(self.mystate2.id) is str)
        self.assertTrue(self.mystate1.id != self.mystate2.id)
        test_created1 = self.test.created_at
        test_created2 = self.mystate2.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

    """
    Test inherited methods.
    """
    def test_save(self):
        test_updated = self.mystate1.updated_at
        self.mystate1.save()
        updated_save = self.mystate1.updated_at
        self.assertFalse(test_updated == updated_save)


if __name__ == '__main__':
    unittest.main()