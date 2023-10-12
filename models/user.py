#!/usr/bin/python3
"""
module User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ user that inherits from BaseModel
    defines attributes """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
