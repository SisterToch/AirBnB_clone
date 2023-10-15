#!/usr/bin/python3
"""
this is the module for the storage

it makes links with the basemodel, the review, state
"""
import json
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.base_model import BaseModel


cls_dict = {

                "User": User,
                "City": City,
                "Place": Place,
                "BaseModel": BaseModel,
                "State": State,
                "Review": Review,
                "Amenity": Amenity
        }


class FileStorage:
    """
    this is the class for the file storage
    details are included in the code
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        set in the object with the key "obj class name" and the id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        this function saves the instance of the class
        in the serial list
        """
        serial = {}
        for key, value in FileStorage.__objects.items():
            serial[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serial, f)

    def reload(self):
        """
        this is to reload an instance already entered
        by the client or other person
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as r:
                loaded_file = json.load(r)
                for key, value in loaded_file.items():
                    class_key = value["__class__"]
                    if class_key in cls_dict.keys():
                       self.new(cls_dict[class_key](**value))

        except FileNotFoundError:
            pass
