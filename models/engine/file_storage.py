#!/usr/bin/python3
"""Define the File storage class."""

import json
import os
from datetime import *
from models import *
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self, obj):
        """Returns the dictionary objects."""
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        FileStorage.__objects[key] = obj

    def new(self, obj):
        """ create """
        FileStorage.__objects.update({obj.id: obj})

    def save(self):
        """serialize __objects to the JSON file __file_path."""
        dict_obj = FileStorage.__objects
        obj_dict = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, mode='r') as f:
                    obj_dict = json.load(f)
                    for o in obj_dict.values():
                        class_name = o["__class__"]
                        del o["__class__"]
                        self.new(eval(class_name)(**o))

            except FileNotFoundError:
                raise FileNotFoundError("File not found")
