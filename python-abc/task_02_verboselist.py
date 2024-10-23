#!/usr/bin/python3
"""
This module provides a VerboseList class that logs
operations when items are added, removed, or popped.
"""


class VerboseList(list):
    """
    class VerboseList inherited from list class
    """
    def append(self, item):
        """
        Add an item to the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extend the list with multiple items and print a message.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a message.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Pop an item from the list by index (default is last item)
        and print a message.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
