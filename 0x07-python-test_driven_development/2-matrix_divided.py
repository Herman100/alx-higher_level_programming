#!/usr/bin/python3


"""
This module provides a function to divide all
elements of a matrix by a given number.

Example:
    >>> matrix = [[1, 2], [3, 4]]
    >>> matrix_divided(matrix, 2)
    [[0.5, 1.0], [1.5, 2.0]]

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    :param matrix: list of lists of integers/floats
    :param div: integer/float
    :return: new matrix with all elements divided
    by div and rounded to 2 decimal places
    """
    if not matrix:
        return []
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
