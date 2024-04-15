#!/usr/bin/python3
"""file_storage moduel contains the FileStorage class"""
import json


class FileStorage():
    """The class FileStorage  that serializes instances to\
        a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return FileStorage.__objects 'all storage objects list'"""
        return FileStorage.__objects

    def new(self, obj):
        """Add the new object to the objects list"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.all()[key] = obj

    def save(self):
        """save the objects list as a json file"""
        json_dict = {}
        for key, value in self.all().items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as fp:
            json.dump(json_dict, fp)

    def reload(self):
        """Reload the objects list from the json file"""

        try:
            with open(self.__file_path, "r") as fp:
                json_dict = json.load(fp)
        except FileNotFoundError:
            return
        for key, value in json_dict.items():
            self.all()[key] = self.create_object(value["__class__"])(**value)

    @staticmethod
    def create_object(class_name):
        """Create an instance from a class name"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                      "City": City, "Amenity": Amenity, "Place": Place,
                      "Review": Review}
        return class_dict[class_name]
