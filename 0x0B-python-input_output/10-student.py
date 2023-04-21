#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 9 - Write a class Student that defines a student by:
    Public instance attributes:
        first_name
        last_name
        age
Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
Public method def to_json(self):
    that retrieves a dictionary representation of a Student
    instance (same as 8-class_to_json.py)
"""


class Student:
    """
    student class containing first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method that retrieves dictionary repr of Student
        """
        dict_allattr = self.__dict__
        if type(attrs) == list and \
                all(isinstance(item, str) for item in attrs):
            dict_allattr2 = \
                {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return dict_allattr2
        return dict_allattr
