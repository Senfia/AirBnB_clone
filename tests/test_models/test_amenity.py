#!/usr/bin/python3
""" Tests the Amenity Subclass """
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """ Testing the Amenity """
    def setUp(self):
        """ Create instances """
        self.free_water = Amenity()
        self.free_wifi = Amenity()
        self.free_wifi.save()

    def test_setup(self):
        """ Test setup """
        self.assertTrue(self.free_water.id != self.free_wifi.id)
        self.assertFalse(hasattr(self.free_water, "updated_at"))
        self.assertTrue(hasattr(self.free_water, "name"))
        self.assertTrue(hasattr(self.free_wifi, "name"))
        self.assertTrue(self.free_water.created_at !=
                        self.free_wifi.created_at)

    def test_types(self):
        """ Types testing """
        self.assertTrue(type(self.free_water.created_at) is
                        datetime.datetime)
        self.assertTrue(type(self.free_water.name) is str)
        a_json = self.free_water.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

    def test_save(self):
        """ Updates testings"""
        b_date = self.free_wifi.updated_at
        self.free_wifi.save()
        b_date2 = self.free_wifi.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
