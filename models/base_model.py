#!/usr/bin/python3

"""
This is module containing the base class for all other classes
"""

import uuid
import datetime
from models import storage

class BaseModel:
    """This is the base class"""
    
    def __init__(self, *args, **kwargs):
        """The initializer function"""

        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                self.__dict__[k] = v

                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of this object"""

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Set the updated_at attribute on this object"""

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dit__ attribute"""

        properties = self.__dict__.copy()
        properties["__class__"] = type(self).__name__
        properties["created_at"] = properties["created_at"].isoformat()
        properties["updated_at"] = properties["updated_at"].isoformat()

        return properties

