#!/usr/bin/python3
"""
This is Amenity class unittest module. This class tests Amenity class.
"""
import unittest
import uuid
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Create object of Amenity class for testing.
    """
    def setUp(self):
        self.water = Amenity()
        self.wifi = Amenity()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.water, "name"))
        self.assertFalse(hasattr(self.wifi, "place"))
        self.assertTrue(type(self.water.name) is str)
        self.assertTrue(type(self.wifi.id) is str)
        self.assertTrue(self.water.id != self.wifi.id)
        test_created1 = self.water.created_at
        test_created2 = self.wifi.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

    """
    Test inherited methods.
    """
    def test_save(self):
        test_updated = self.water.updated_at
        self.water.save()
        updated_save = self.water.updated_at
        self.assertFalse(test_updated == updated_save)

    """
    Test dynamic method creation
    """
    def test_count(self):
        self.assertFalse(hasattr(self.water, "do_count()"))


if __name__ == '__main__':
    unittest.main()
