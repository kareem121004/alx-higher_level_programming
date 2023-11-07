#!/usr/bin/python3
"""save_to_json_file()"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
