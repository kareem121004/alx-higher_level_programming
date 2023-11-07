#!/usr/bin/python3
"""oad_from_json_file()"""

import json


def load_from_json_file(filename):
    """loads an object to from JSON file"""

    with open(filename, 'r') as f:
        return (json.load(f))
