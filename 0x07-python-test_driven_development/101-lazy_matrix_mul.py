#!/usr/bin/python3
"""This module defines a function that multiplies two matrices using NumPy."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""
    return np.matmul(m_a, m_b)
