#!/usr/bin/python3
""" MyInt class """


class MyInt(int):
    """ Inverted == and != """

    def __eq__(self, other):
        """ Invert == """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Invert != """
        return super().__eq__(other)
