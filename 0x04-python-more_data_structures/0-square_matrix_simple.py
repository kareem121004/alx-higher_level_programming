#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = []
        for element in row:
            square = element ** 2
            squared_row.append(square)
        result.append(squared_row)
    return result
