#!/usr/bin/python3

def islower(c):
    """Check if a character is lowercase."""
    # Get the ASCII value of the character
    ascii_value = ord(c)
    # Check if the ASCII value is within the range for lowercase letters
    if 97 <= ascii_value <= 122:
        return True
    else:
        return False
