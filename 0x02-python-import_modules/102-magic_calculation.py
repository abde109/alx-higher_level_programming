#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)


if __name__ == "__main__":
    """Demonstrates the magic_calculation function."""
    from sys import argv

    if len(argv) != 3:
        print("Usage: ./102-magic_calculation.py <a> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[2])
    result = magic_calculation(a, b)

    print(result)
