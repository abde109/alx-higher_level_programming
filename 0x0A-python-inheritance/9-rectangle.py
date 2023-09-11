#!/usr/bin/python3
""" Full Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle with more features """

    def __init__(self, width, height):
        """ Initialize """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate area """
        return self.__width * self.__height

    def __str__(self):
        """ String representation """
        return f"[Rectangle] {self.__width}/{self.__height}"
