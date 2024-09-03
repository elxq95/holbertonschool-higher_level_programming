#!/usr/bin/python3

alphabet = "".join([chr(i) for i in range(97, 123)])

modified_alphabet = ""

for char in alphabet:
    if char == 'q' or char == 'e':
        continue
    modified_alphabet += char

print("{}".format(modified_alphabet), end="")
