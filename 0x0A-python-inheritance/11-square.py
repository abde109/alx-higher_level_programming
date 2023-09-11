#!/usr/bin/python3
""" Enhanced Square class """
Rectangle = __import__('9-rectangly').Rectangle


class Square(Rectangle):
    """ More features for Square """

    def __init__(self, size):
        """ Initialize """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """ String representation """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
