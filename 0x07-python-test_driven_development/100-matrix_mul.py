#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrices

    Args:
        m_a (list of lists of ints/floats): The first matrix
        m_b (list of lists of ints/floats): The second matrix
    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints/floats
        TypeError: If m_a or m_b is empty
        TypeError: If m_a or m_b has different-sized rows
        ValueError: If m_a and m_b cannot be multiplied
    Returns:
        A new matrix representing the multiplication of m_a by m_b
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    _b = []
    for r in range(len(m_b[0])):
        _row = []
        for c in range(len(m_b)):
            _row.append(m_b[c][r])
        _b.append(_row)

    _matrix = []
    for row in m_a:
        _row = []
        for col in _b:
            prod = 0
            for i in range(len(_b[0])):
                prod += row[i] * col[i]
            _row.append(prod)
        _matrix.append(_row)

    return _matrix
