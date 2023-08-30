#!/usr/bin/python3
"""This module defines a class Square that can be printed."""


class Square:
    # (Same as Task 6, but add the following method)
    def __str__(self):
        """Returns a string representation of the square."""
        if self.size == 0:
            return ""
        return "\n".join([" " * self.position[0] + "#" * self.size for _ in range(self.size)])
