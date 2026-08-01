#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line
    """
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:c}".format(ord(c)), end="")
    print()
