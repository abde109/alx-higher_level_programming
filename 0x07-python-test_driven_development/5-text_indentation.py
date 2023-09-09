#!/usr/bin/python3
"""This module defines a function that indents text based on specific characters."""

def text_indentation(text):
    """Print a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line:
        print(line.strip())

