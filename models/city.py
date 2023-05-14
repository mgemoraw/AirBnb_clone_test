#!/usr/bin/python3
"""City Module for AirBnB project"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class contains state Id and name of the city"""
    state_id = ""
    name = ""
