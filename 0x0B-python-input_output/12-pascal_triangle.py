#!/usr/bin/python3
"""12-pascal_triangle: pascal_triangle()"""


def pascal_triangle(n):
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            previous_row = triangle[i - 1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(previous_row[j - 1] + previous_row[j])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
