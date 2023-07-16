#!/usr/bin/python3
"""
This class tests City class.
"""
import unittest
import uuid
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """
    Create and test an object of the city class.
    """
    def setUp(self):
        self.city1 = City()
        self.city2 = City()

    """
    Test attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertFalse(hasattr(self.city2, "place"))
        self.city2.place = ""
        self.assertTrue(hasattr(self.city2, "place"))
        self.assertTrue(type(self.city1.state_id) is str)
        self.assertTrue(type(self.city1.name) is str)
        self.assertTrue(type(self.city2.place) is str)
        self.assertTrue(type(self.city2.id) is str)
        self.assertTrue(self.city1.id != self.city2.id)
        test_created1 = self.city1.created_at
        test_created2 = self.city2.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

    """
    Test inherited methods.
    """
    def test_save(self):
        test_updated = self.city1.updated_at
        self.city1.save()
        updated_save = self.city1.updated_at
        self.assertFalse(test_updated == updated_save)

if __name__ == '__main__':
    unittest.main()