#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 11 - In addition to task 10:
    Public method def reload_from_json(self, json):
    that replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
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
    
    def reload_from_json(self, json):
        """
        This method replaces all attributes
        of the Student instance
        """
        for k, v in json.items():
            setattr(self, k, v)
