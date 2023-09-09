#!/usr/bin/python3
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    
    # Validation checks for m_a and m_b
    for name, matrix in [("m_a", m_a), ("m_b", m_b)]:
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not matrix or not all(row for row in matrix):
            raise ValueError(f"{name} can't be empty")
        if not all(isinstance(el, (int, float)) for row in matrix for el in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError(f"each row of {name} must should be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
