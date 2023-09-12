#!/usr/bin/python3
"""Returns a dictionary description for JSON serialization."""


def class_to_json(obj):
    """Return a dictionary description of an object."""
    return obj.__dict__
