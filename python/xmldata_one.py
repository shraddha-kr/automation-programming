"""
https://www.guru99.com/manipulating-xml-with-python.html
The easiest way to quickly load an XML document and to create a minidom object using the xml.dom module. The minidom object provides a simple parser method that quickly creates a DOM tree from the XML file.
"""
import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("./python/myxmlone.xml")  
    print(doc.nodeName)
    print(doc.firstChild.tagName)    

    # Write XML Node
    newexpertise = doc.createElement("expertise")
    newexpertise.setAttribute("name", "BigData")
    doc.firstChild.appendChild(newexpertise)
    print(" ")

    # Parse XML 
    expertise = doc.getElementsByTagName("expertise")
    print("%d expertise:" % expertise.length)
    for skill in expertise:        
        print(skill.getAttribute("name"))
        
if __name__ =="__main__":
    main()