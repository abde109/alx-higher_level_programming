#!/usr/bin/python3
"""This module defines a class Square with comparators."""


class Square:
    """This class defines a square with a size that can be compared."""
    def __init__(self, size=0):
        """Initialize the square with a size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if one square is less than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square is less than or equal to another."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if one square is greater than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square is greater than or equal to another."""
        return self.area() >= other.area()
