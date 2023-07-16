#!/usr/bin/python3
"""
This is Place class unittest module. This class tests Place class.
"""
import unittest
import uuid
import datetime
from models.place import Place


class TestBaseModel(unittest.TestCase):
    """
    Create object of Place class for testing.
    """
    def setUp(self):
        self.myplace1 = Place()
        self.myplace2 = Place()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.myplace1, "city_id"))
        self.assertTrue(hasattr(self.myplace1, "number_rooms"))
        self.assertTrue(hasattr(self.myplace1, "number_bathrooms"))
        self.assertTrue(hasattr(self.myplace1, "latitude"))
        self.assertTrue(hasattr(self.myplace1, "longitude"))
        self.assertTrue(hasattr(self.myplace1, "amenities"))
        self.assertTrue(hasattr(self.myplace1, "max_guest"))
        self.assertFalse(hasattr(self.myplace1, "no_guest"))
        self.assertTrue(hasattr(self.myplace1, "description"))
        self.assertTrue(hasattr(self.myplace1, "price_by_night"))
        self.assertTrue(hasattr(self.myplace1, "user_id"))
        self.assertTrue(hasattr(self.myplace1, "name"))
        self.assertTrue(type(self.myplace1.number_rooms) is int)
        self.assertTrue(type(self.myplace1.number_bathrooms) is int)
        self.assertTrue(type(self.myplace1.price_by_night) is int)
        self.assertTrue(type(self.myplace1.max_guest) is int)
        self.assertTrue(type(self.myplace1.latitude) is float)
        self.assertTrue(type(self.myplace1.longitude) is float)
        self.assertTrue(type(self.myplace1.name) is str)
        self.assertTrue(type(self.myplace1.city_id) is str)
        self.assertTrue(type(self.myplace1.user_id) is str)
        self.assertTrue(type(self.myplace1.description) is str)
        self.assertTrue(type(self.myplace1.amenities) is list)
        self.assertTrue(type(self.myplace1.id) is str)
        self.assertTrue(self.myplace1.id != self.myplace2.id)
        test_created1 = self.myplace1.created_at
        test_created2 = self.myplace2.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

    """
    Test inherited methods.
    """
    def test_save(self):
        test_updated = self.myplace1.updated_at
        self.myplace1.save()
        updated_save = self.myplace1.updated_at
        self.assertFalse(test_updated == updated_save)


if __name__ == '__main__':
    unittest.main()
