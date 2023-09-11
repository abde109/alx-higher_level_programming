#!/usr/bin/python3
""" Square class """
Rectangle = __import__('9-rectangly').Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle """

    def __init__(self, size):
        """ Initialize """
        self.integer_validator("size", size)
        super().__init__(size, size)
