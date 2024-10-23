#!/usr/bin/python3
"""This module demonstrates in reading data from one
format (CSV) and converting it into another format (JSON)
using serialization techniques
"""
from csv import DictReader
import json


def convert_csv_to_json(csv_file):
    try:
        if csv_file:
            with open(csv_file, 'r') as f:
                my_dict = DictReader(f)
                list_dict = list(my_dict)

            with open('data.json', 'w') as file:
                json.dump(list_dict, file)
            print("Conversion successful!")
            return True
        else:
            return False
    except FileNotFoundError:
        return False