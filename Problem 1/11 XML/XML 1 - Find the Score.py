import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):

    node_attribues = len(node.attrib)
    child_attributes = sum(get_attr_number(child) for child in node)
    result = node_attribues + child_attributes

    return result


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))