#!/usr/bin/python3
"""Saves an object to a file in JSON format."""

import json

def save_to_json_file(my_obj, filename):
    """Save an object as a JSON string in a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
