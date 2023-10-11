#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """set in the object with the key "obj class name" and the id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__object[key] = obj
    def save(self):
        serial = {}
        for key, value in self.__objects.items():
            serial[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding = "utf-8") as f:
            json.dump(serial, f)
    def reload(self):
        try:
            with open(self.__file_path, "r", encoding = "utf-8") as r:
                load = json.load(r)
                for key, value in load.items():
                    class_name, obj_id = key.split(".")

