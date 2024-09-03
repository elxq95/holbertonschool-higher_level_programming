#!/usr/bin/python3

alphabet = ""

for i in range(97, 123):
    if i != 113 and i != 101:
        alphabet += chr(i)

print("{}".format(alphabet), end="")
