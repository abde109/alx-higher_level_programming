#!/usr/bin/python3
""" Check if subclass """


def inherits_from(obj, a_class):
    """ Is it a subclass? """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
