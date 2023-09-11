#!/usr/bin/python3
""" Add attribute """


def add_attribute(obj, name, value):
    """ Add if possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
