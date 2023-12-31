#!/usr/bin/python3
"""Converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object."""
    return json.dumps(my_obj)
