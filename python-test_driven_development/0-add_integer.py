def add_integer(a, b=98):
    """
    Adds two integers or floats, ensuring that float overflow is handled.
    If a or b is not an integer or float, raises TypeError.
    If the float value is 'inf' or 'nan', raises appropriate exceptions.
    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle float overflow and invalid numbers
    if isinstance(a, float) and (a == float('inf') or a == float('-inf') or a != a):
        raise OverflowError("cannot convert float infinity or NaN to integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf') or b != b):
        raise OverflowError("cannot convert float infinity or NaN to integer")

    # Convert floats to integers before adding
    a = int(a)
    b = int(b)

    return a + b
