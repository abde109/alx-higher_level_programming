#!/usr/bin/python3
"""Defines a Student class with a method to retrieve filtered attributes."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a filtered dictionary description."""
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    filtered_dict[attr] = self.__dict__[attr]
            return filtered_dict
