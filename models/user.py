#!/usr/bin/python3
"""
User class to represent the user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Subclass that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
