#!/usr/bin/python3
def fizzbuzz():
    """
    Prints the numbers from 1 to 100 separated by a space
    Multiples of 3: Fizz, multiples of 5: Buzz,
    multiples of both: FizzBuzz
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
