#!/usr/bin/python3
"""
This module provides a function that returns
the sound made by an animal, either 'Bark' or 'Meow'.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses.
        Each animal should return its sound.
        """
        pass

class Dog(Animal):

    def sound(self):
        return "Bark"
class Cat(Animal):

    def sound(self):
        return "Meow"
