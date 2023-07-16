#!/usr/bin/python3
"""This module contains the base model
    from which all others class will inherit
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """The base class for all others"""

    def __init__(self, *args, **kwargs):
        """The initializer"""

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of this class"""

        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """Return a string representation of this object"""

        return (self.__str__())

    def save(self):
        """The save method for this object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dict representation of this object"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
