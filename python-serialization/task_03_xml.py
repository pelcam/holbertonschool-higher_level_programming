#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function that serialize a python dictionary to xml
    """

    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    with open(filename, 'wb') as file:
        tree.write(file, xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Function that deserialize from xml
    """

    try:
        root = ET.parse(filename).getroot()
        data = {}
        for child in root:
            data[child.tag] = child.text
        return data
    except (ET.ParseError, FileNotFoundError) as e:
        print("Error reading {}: {}".format(filename, e))
        return {}
