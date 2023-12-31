#!/usr/bin/python3
"""This module defines the square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.
        Calls the constructor of the Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the 'size' attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the 'size' attribute.
        Sets both width and height to the given size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overloaded string representation of the Square object.
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Update method to set attributes.
        """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to return the dictionary representation of the Square object.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
