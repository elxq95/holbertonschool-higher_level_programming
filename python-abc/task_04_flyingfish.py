#!/usr/bin/python3
"""
This module provides a FlyingFish class that logs
operations when items are added, removed, or popped.
"""
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    class FlyingFish inherited from list class
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
