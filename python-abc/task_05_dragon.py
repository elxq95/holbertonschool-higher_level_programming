#!/usr/bin/python3
"""
This module provides SwimMixin and FlyMixin class that print
specific messages. The Dragon class is inherited from SwimMixin
and FlyMixin
"""
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
