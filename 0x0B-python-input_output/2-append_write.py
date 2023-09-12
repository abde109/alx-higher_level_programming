#!/usr/bin/python3
"""Appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a file and return the character count."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
