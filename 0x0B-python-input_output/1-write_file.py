#!/usr/bin/python3
"""Writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a file and return the character count."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
