#!/usr/bin/python3
"""
This module constains the review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class"""
    place_id = ""
    user_id = ""
    text = ""
