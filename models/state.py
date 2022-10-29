#!/usr/bin/python3

""" This module creates a 'user' class """

from models.base_model import BaseModel


class State(BaseModel):

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
