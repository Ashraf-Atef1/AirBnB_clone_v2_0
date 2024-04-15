#!/usr/bin/python3
"""The module contains the class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
