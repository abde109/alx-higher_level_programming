#!/usr/bin/python3
""" MyList class """

class MyList(list):
    """ Print sorted list """
    def print_sorted(self):
        print(sorted(self))
