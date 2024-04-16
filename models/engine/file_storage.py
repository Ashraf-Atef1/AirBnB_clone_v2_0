#!/usr/bin/python3
"""file_storage moduel contains the FileStorage class"""
import json


class FileStorage():
    """The class FileStorage  that serializes instances to\
        a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return FileStorage.__objects 'all storage objects list'"""
        if cls is None:
            return FileStorage.__objects
        else:
            new_obj = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    new_obj[key] = value
            return new_obj

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

    def delete(self, obj=None):
        """remove first matching object from __objects"""
        if obj:
            to_del = None
            for key, value in self.__objects.items():
                if value == obj:
                    to_del = key
                    break
            if to_del:
                del self.__objects[to_del]

    @staticmethod
    def all_classes():
        """Get all models to help in convert string to class"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}

    def create_object(self, class_name):
        """Create an instance from a class name"""
        return self.all_classes()[class_name]
