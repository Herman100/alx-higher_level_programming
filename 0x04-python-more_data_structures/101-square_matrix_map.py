#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
  Computes the square value of all integers of a matrix using map.

  Args:
    matrix: A 2-dimensional array.

  Returns:
    A new matrix:
      Same size as matrix
      Each value should be the square of the value of the input
    Initial matrix should not be modified

  Raises:
    ValueError: If the matrix is not a 2-dimensional array.
    """

    if not isinstance(matrix, list):
        raise ValueError("matrix must be a list")

    if len(matrix) == 0:
        return []

    if len(matrix[0]) == 0:
        return []

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)

    return new_matrix
