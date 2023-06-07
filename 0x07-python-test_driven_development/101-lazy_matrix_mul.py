#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists): The first matrix to be multiplied.
        m_b (list of lists): The second matrix to be multiplied.

    Returns:
        numpy.ndarray: The result of the multiplication of the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list of lists or if their elements are not integers or floats.
        ValueError: If m_a or m_b is empty or if their shapes are not compatible for multiplication.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a should be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b should be a list of lists")
    if not all(isinstance(e, (int, float)) for row in m_a for e in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(e, (int, float)) for row in m_b for e in row):
        raise TypeError("m_b should contain only integers or floats")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b)
