#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{}".format(chr(i - ((i - 97 + 1) % 2 * 32))), end="")
