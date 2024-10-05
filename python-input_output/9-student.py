#!/usr/bin/python3
"""This module handles a class called Student. It has constructor
method for instantiation
"""


class Student:
    """A class called Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
