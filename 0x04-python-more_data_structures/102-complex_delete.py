#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_value = []
    for key, val in a_dictionary.items():
        if val == value:
            key_value.append(key)
    for key in key_value:
        a_dictionary.pop(key)
    return a_dictionary
