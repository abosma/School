stations = ["Schagen","Heerhugowaard", "Alkmaar", "Castricum", "Zaandam","Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]

beginstation = input("Wat is het beginstation: ");

if str(beginstation) in stations:
    print("");
else:
    beginstation = "Schagen";
    print("Dit station is niet geldig, beginstation is: " + beginstation);

eindstation = input("Wat is het eindstation: ");

if str(eindstation) in stations:
    if stations.index(eindstation) > stations.index(beginstation):
        print("");
    else:
        eindstation = "Maastricht";
        print("Dit is niet geldig, jouw eindstation is: " + eindstation);
else:
    eindstation = "Maastricht";
    print("Dit is niet geldig, jouw eindstation is: " + eindstation);

print("Het beginstation " + beginstation + " is het " + str(stations.index(beginstation) + 1) + "e station in het traject");

print("Het eindstation " + eindstation + " is het " + str(stations.index(eindstation) + 1) + "e station in het traject");

afstand = abs((stations.index(beginstation) + 1) - (stations.index(eindstation) + 1));

print("De afstand bedraagt " + str(afstand) + " station(s)");

prijs = afstand * 5;

print("De prijs van het kaartje is " + str(prijs) + " euro.");

print("Jij stapt in de trein in: " + str(beginstation));

for x in range(1, afstand):
    print("     - " + stations[stations.index(beginstation) + x]);

print("Jij stapt uit in: " + str(eindstation));