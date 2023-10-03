#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            result_str += uppercase_char
        else:
            result_str += char
    print(result_str)
