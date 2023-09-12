#!/usr/bin/python3
"""Adds arguments to a Python list and saves to a file."""
import json
from sys import argv


def add_arguments():
    """Add CLI arguments to list and save as JSON."""
    filename = "add_item.json"
    try:
        with open(filename, "r") as f:
            my_list = json.load(f)
    except FileNotFoundError:
        my_list = []

    my_list.extend(argv[1:])
    with open(filename, "w") as f:
        json.dump(my_list, f)

if __name__ == "__main__":
    add_arguments()
