#!/usr/bin/python3
"""This module handles a class called Student. It has constructor
method for instantiation
"""


class Student:
    """A class called Student
    function to_json
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            new_dict = dict()
            for element in attrs:
                if element in self.__dict__:
                    new_dict[element] = self.__dict__[element]
            return new_dict
