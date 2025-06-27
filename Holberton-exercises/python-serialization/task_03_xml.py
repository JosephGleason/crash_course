#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename)

        return True  # Success
    except Exception:
        return False  # Something went wrong

def deserialize_from_xml(filename):
    try:
        # Load XML from file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Extract tag names and values
        result = {}
        for element in root:
            result[element.tag] = element.text

        return result

    except Exception:
        return None
