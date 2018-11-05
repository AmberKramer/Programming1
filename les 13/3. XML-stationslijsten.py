import xmltodict
def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary
dict = processXML("stations.xml")
treininfo = dict['Stations']['Station']
print('Dit zijn de codes en types van de 4 stations:')
for info in treininfo:
    print('{:4} - {}'.format(info['Code'],info['Type']))
print('\nDit zijn alle stations met één of meer synoniemen:')
for info in treininfo:
    if info['Synoniemen'] is not None:
        print('{:4} - {}'.format(info['Code'], info['Synoniemen']))
print('\nDit is de lange naam van elk station:')
for info in treininfo:
    print('{:4} - {}'.format(info['Code'],info['Namen']['Lang']))