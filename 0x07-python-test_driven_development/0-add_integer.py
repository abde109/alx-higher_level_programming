#!/usr/bin/python3
"""This module defines a function that adds two integers or floats."""


def add_integer(a, b=98):
    """Return the integer addition of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf') or b == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if a != a or b != b:
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)

