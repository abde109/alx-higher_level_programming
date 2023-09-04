#!/usr/bin/python3
"""This module defines a function that prints a square."""

def print_square(size):
    """Print a square with the character #."""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
