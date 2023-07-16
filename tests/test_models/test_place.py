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
        self.labone = Place()
        self.osu = Place()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.labone, "city_id"))
        self.assertTrue(hasattr(self.labone, "number_rooms"))
        self.assertTrue(hasattr(self.labone, "number_bathrooms"))
        self.assertTrue(hasattr(self.labone, "latitude"))
        self.assertTrue(hasattr(self.labone, "longitude"))
        self.assertTrue(hasattr(self.labone, "amenities"))
        self.assertTrue(hasattr(self.labone, "max_guest"))
        self.assertFalse(hasattr(self.labone, "no_guest"))
        self.assertTrue(hasattr(self.labone, "description"))
        self.assertTrue(hasattr(self.labone, "price_by_night"))
        self.assertTrue(hasattr(self.labone, "user_id"))
        self.assertTrue(hasattr(self.labone, "name"))
        self.assertTrue(type(self.labone.number_rooms) is int)
        self.assertTrue(type(self.labone.number_bathrooms) is int)
        self.assertTrue(type(self.labone.price_by_night) is int)
        self.assertTrue(type(self.labone.max_guest) is int)
        self.assertTrue(type(self.labone.latitude) is float)
        self.assertTrue(type(self.labone.longitude) is float)
        self.assertTrue(type(self.labone.name) is str)
        self.assertTrue(type(self.labone.city_id) is str)
        self.assertTrue(type(self.labone.user_id) is str)
        self.assertTrue(type(self.labone.description) is str)
        self.assertTrue(type(self.labone.amenities) is list)
        self.assertTrue(type(self.labone.id) is str)
        self.assertTrue(self.labone.id != self.osu.id)
        test_created1 = self.labone.created_at
        test_created2 = self.osu.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

    """
    Test inherited methods.
    """
    def test_save(self):
        test_updated = self.labone.updated_at
        self.labone.save()
        updated_save = self.labone.updated_at
        self.assertFalse(test_updated == updated_save)


if __name__ == '__main__':
    unittest.main()
