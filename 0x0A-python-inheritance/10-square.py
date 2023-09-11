#!/usr/bin/python3
""" Square class """
from 9-rectangle import Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle """

    def __init__(self, size):
        """ Initialize """
        self.integer_validator("size", size)
        super().__init__(size, size)
