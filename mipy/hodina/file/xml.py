import xml.etree.ElementTree as ET

tree = ET.parse("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sample.xml")

root = tree.getroot()

for child in root:
    print(child.attrib)