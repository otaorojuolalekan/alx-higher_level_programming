#!/usr/bin/python3
"""
The AirBnB project is a big part of the Higher level curriculum.
This project will help you be ready for it.
All previous lessons learnt will come to use here.
"""
import json


class Base:
    """
    This is the base class of the Airbnb mini project
    Attrs:
        nb_objects --> private attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiation for Base class
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # task 15
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dict"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    # task 16
    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        fname = cls.__name__ + ".json"
        with open(fname, "w", encoding="utf-8") as fp:
            if list_objs is None or list_objs == []:
                fp.write('[]')
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                fp.write(Base.to_json_string(dict_list))
