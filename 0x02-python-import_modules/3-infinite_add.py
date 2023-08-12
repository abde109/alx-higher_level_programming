#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""
    from sys import argv

    result = 0
    for arg in argv[1:]:
        result += int(arg)

    print(result)
