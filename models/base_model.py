#!/usr/bin/python3

"""
This is module containing the base class for all other classes
"""

import uuid
import datetime

class BaseModel:
    """This is the base class"""

    __name__
    
    def __init__(self):
        """The initializer function"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of this object"""

        return f'[{self.name}] ({self.id}) {self.__dict__}'
    
    def save(self):
        """Set the updated_at attribute on this object"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the __dit__ attribute"""

        properties = self.__dict__.copy()
        properties["__class__"] = type(self).__name__
        properties["created_at"] = properties["created_at"].isoformat()
        properties["updated_at"] = properties["updated_at"].isoformat()

        return properties
