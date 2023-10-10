#!/usr/bin/python3
"""
module Review that defines th reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class that defines the reviews """

    place_id = ""
    user_id = ""
    text = ""
