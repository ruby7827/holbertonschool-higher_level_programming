#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line
    """
    for c in str:
        code = ord(c) - 32 if 97 <= ord(c) <= 122 else ord(c)
        print("{:c}".format(code), end="")
    print()
