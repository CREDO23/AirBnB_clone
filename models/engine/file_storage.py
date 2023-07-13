#!/usr/bin/python3
"""This module contains the self class"""

import json
import os

class FileStorage:
    """The self class"""

    __file_path = "file.json"
    __objects = {}
    classes = {}

    def __init__(self):
        """Constructor"""

    def all(self):
        """Returns all objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w", encoding="utf-8") as write:
            data = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(data, write)
        
    def avClasses(self):
        """Returns all availble classes"""

        from models.base_model import BaseModel

        classes = {
            "BaseModel": BaseModel
        }

        return classes

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "r", encoding="utf-8") as f:
            objc_dict = json.load(f)
            objc_dict = {k : self.avClasses()[v["__class__"]](**v) for k, v in objc_dict.items()}
            self.__objects = objc_dict
    