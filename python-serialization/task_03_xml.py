#!/usr/bin/python3
"""This module demonstrates serialization and
deserialization using XML as an alternative format to JSON
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    new_dict = {}
    for element in root:
        new_dict[element.tag] = element.text
    return new_dict
