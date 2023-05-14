#!/usr/bin/python3
"""defines class to manage storage of files"""
import json


class FileStorage:
    """Class that manages stoage of hbnb models"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models that are currently on storage"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obje.to_dict()['__class__'] + "." + obj.id: obj})
    
    def save(self):
        """Saves storage dictionary to a file"""
        with open(FileStorage.__file_path, "w") as file:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, file)
    def reload(self):
        pass
     