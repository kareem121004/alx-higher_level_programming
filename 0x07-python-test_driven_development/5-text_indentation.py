#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", "?", ":"]
    lines = []

    current_line = ""
    for char in text:
        current_line += char
        if char in punctuations:
            lines.append(current_line.strip())
            lines.append("")
            current_line = ""
    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
