#!/usr/bin/python3
"""This module is HBNB Console """
import cmd
import sys
from models.base_model import BaseModel
# from models.__init__ import Storage
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    # """HBNB Command class"""
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Review': Review
              }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print("(hbnb)")

    def precmd(self, line):
        _cmd = _cls = _id = _args = ""
        if not ("." in line and "(" in line and ")" in line):
            return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
