#!/usr/bin/python3
"""
FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
              "State": State, "City": City, "Amenity": Amenity,
              "Review": Review}


class FileStorage:
    """
    define some method and attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        returns the dictionary __objects
        """
        if cls is None:
            return self.__objects
        else:
            s = {}
            for k, v in self.__objects.items():
                if cls == v.__class__ or cls == v.__class__.__name__:
                    s[k] = v
            return s

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict1 = {}
        for k, v in FileStorage.__objects.items():
            dict1[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dict1, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
            for key, value in data.items():
                class_name = value["__class__"]
                for i, j in class_dict.items():
                    if class_name == i:
                        FileStorage.__objects[key] = j(**value)
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """
        Deletes the object
        """
        if obj is not None:
            del FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                                     obj.id)]

    def close(self):
        """
        deserializing
        """
        self.reload()
