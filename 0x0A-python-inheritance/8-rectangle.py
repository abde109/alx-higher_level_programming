#!/usr/bin/python3
""" Rectangle class """


class Rectangle(BaseGeometry):
    """ Rectangle inherits BaseGeometry """
    
    def __init__(self, width, height):
        """ Initialize """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
