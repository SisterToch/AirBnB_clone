#!/usr/bin/python3
"""
the module is for reviews by clients
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """you can make your review here"""
    place_id = ""
    user_id = ""
    text = ""
