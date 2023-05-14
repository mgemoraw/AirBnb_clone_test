#!/usr/bin/python3
"""Defines base model for all classes"""
import uuid
from datetime import datetime


class BaseModel:
    """base model for hbnb models"""
    def __init__(self, *args, **kwargs):
        """model constructor"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['upated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Retrns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split("\"")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)