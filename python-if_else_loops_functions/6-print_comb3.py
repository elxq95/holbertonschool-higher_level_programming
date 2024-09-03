#!/usr/bin/python3

# Outer loop for the first digit (0 to 9)
for i in range(10):
    # Inner loop for the second digit (0 to 9)
    for j in range(i + 1, 10):  # Ensure j is always greater than i to avoid duplicate pairs like (1,0)
        # Print the combination
        if i < 8:  # As long as i is less than 8, it means it's not the last combination
            print("{:02d}, ".format(i * 10 + j), end="")
        else:  # When i is 8, j can only be 9 for the last valid pair (89)
            print("{:02d}".format(i * 10 + j))