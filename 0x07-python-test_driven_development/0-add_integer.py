#!/usr/bin/python3
"""
add_integer:
    Checks if parameters are int
    Returns sum of parameters
"""

def add_integer(a, b=98):
    """
    Checks if int, otherwise return sum
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
