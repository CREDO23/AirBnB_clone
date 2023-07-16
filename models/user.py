#!/usr/bin/python3

"""This module contains the user class"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """The user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
