#!/usr/bin/python3
"""Reads and prints a text file."""


def read_file(filename=""):
    """Read and print a text file (UTF-8)."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
