#!/usr/bin/python3
"""This module defines a function that adds two integers or floats."""


def add_integer(a, b=98):
    """Add two integers or floats, returning an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
