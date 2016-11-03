import xmltodict

#Hier wordt het XML file gelezen en worden de content van de file gereturnd met deze functie
def readXML(xmlfile):
    with open(xmlfile) as myXMLFile:
        xmlString = myXMLFile.read();
        xmldictionary = xmltodict.parse(xmlString);
        return xmldictionary

#Stationsdict is de dictionary met alle dingen in de xml file erin
Stationsdict = readXML("Les8/treinstations.xml");
#Stations is een dict met stations en station contents in de stationsdict var
Stations = Stationsdict["Stations"]["Station"]

#lege lists maken om te appenden
stationCodes = []
stationTypes = []
stationSynoniemen = []
stationNamen = []

#Voor ieder station in stations
for Station in Stations:
    stationCodes.append(Station["Code"]);
    stationTypes.append(Station["Type"]);
    stationSynoniemen.append(Station["Synoniemen"]);
    stationNamen.append(Station["Namen"]["Lang"]);

#Voor 4 stations
print("Dit zijn de codes en types van de 4 stations");
for i in range(4):
    print("{0:5}".format(stationCodes[i]), stationTypes[i], sep=" - ");

#Voor ieder station ins de stations dict waar het variable synoniemen niet leeg is
print("\nDit zijn alle stations met één of meer synoniemen");
for Station in Stations:
    if Station["Synoniemen"] != None:
        #print deze op deze manier
        print("{0:5}".format(Station["Code"]), Station["Synoniemen"], sep=" - ");

print("\nDit is de lange naam van elk station");

#Hier wordt de volle naam van elk station geprint
for i in range(4):
    print("{0:5}".format(stationCodes[i]), stationNamen[i], sep=" - ");
