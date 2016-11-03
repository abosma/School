import xmltodict

def readXML(xmlfile):
    with open(xmlfile) as myXMLFile:
        xmlString = myXMLFile.read()
        xmldictionary = xmltodict.parse(xmlString)
        return xmldictionary

Stationsdict = readXML("Les8/artikels.xml")

for x in Stationsdict["artikelen"]["artikel"]:
    print(x["naam"])