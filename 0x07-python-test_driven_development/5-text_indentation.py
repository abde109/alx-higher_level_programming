#!/usr/bin/python3
"""This module defines a function that indents text based on specific characters."""

def text_indentation(text):
    """Print text with 2 new lines after ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))
