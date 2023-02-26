import xml.etree.ElementTree as ET

tree = ET.parse("./python/myxmltwo.xml")
root = tree.getroot()


print("Expertise Data: ")

for elem in root:
    for subelem in elem:
        print(subelem.text)