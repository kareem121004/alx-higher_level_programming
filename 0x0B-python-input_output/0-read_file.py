#!/usr/bin/python3
"""Defines a function that reads a file"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read())
