#!/usr/bin/python3

"""
This is the module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    this is the function that returns a list of list

    Params:
        matrix: a list of list
        div: an integer to dived the matrix

    Raise:
        TypeError: when matrix is not a list of list of int/float
        TypeError: when rows are not of equal size
        TypeError: when div is not a number
        ZeroDivisionError: when div is `0`

    Return:
        A list of list
    """
    error_msg = {
        "msg1": "matrix must be a matrix (list of lists) of integers/floats",
        "msg2": "Each row of the matrix must have the same size",
        "msg3": "div must be a number",
        "msg4": "division by zero"
        }

    if not all(isinstance(row, list)
               and all(isinstance(element, (int, float))
               for element in row) for row in matrix):
        raise TypeError(error_msg["msg1"])

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(error_msg["msg2"])

    if not isinstance(div, (float, int)):
        raise TypeError(error_msg["msg3"])

    if div == 0:
        raise ZeroDivisionError(error_msg["msg4"])

    new_matrix = list(
            map(lambda row:
                list(map(lambda element:
                         round(element / div, 2), row)),
                matrix)
            )
    return new_matrix
