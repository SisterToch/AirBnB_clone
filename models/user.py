#!/usr/bin/python3
"""
the module for user on the airbnb
"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherits from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
