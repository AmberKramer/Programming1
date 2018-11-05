import xmltodict
def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

dict=processXML("artikelen.xml")
producten=dict['artikelen']['artikel']

for product in producten:
    print(product['naam'])