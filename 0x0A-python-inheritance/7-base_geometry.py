#!/usr/bin/python3
""" BaseGeometry with integer validation """


class BaseGeometry:
    """ With integer_validator """
    
    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """ Validate value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
