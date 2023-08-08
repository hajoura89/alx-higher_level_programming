#!/usr/bin/python3
"""Divide a matrix"""
def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): A list of lists of integers or floats
        div (int/float): The divisor
    Raises:
        TypeError: If matrix contains non numbers
        TypeError: If matrix rows of different sizes
        TypeError: If div not an int or float
        ZeroDivisionError: If div equal to 0
    Returns:
        A new matrix with the result of the division
    """
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    
        if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])