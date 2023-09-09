#!/usr/bin/python3
"""This module defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""
    if not isinstance(matrix, list) or not all
    (isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix of integers/floats")

    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
