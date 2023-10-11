#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    for key, value in new_dir.items():
        new_dir[key] = value * 2
    return new_dir
