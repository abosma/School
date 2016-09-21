stations = ["Schagen","Heerhugowaard", "Alkmaar", "Castricum", "Zaandam","Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]

def inlezen_beginpunt():
    beginstation = input("Wat is het beginstation: ");
    # Terwijl het ingevoerde beginstation niet in de lijst stations zit.
    while (str(beginstation) not in stations):
        # Vraag om een geldig beginstation.
        beginstation = input("Dit station is niet geldig, vul een geldig station in: ");
        # Als deze wel in de lijst stations zit.
    if str(beginstation) in stations:
        # Stuur het ingevoerde beginstation door.
        return beginstation;

def inlezen_eindpunt(begin):
    eindstation = input("Wat is het eindstation: ");
    # Terwijl het ingevoerde eindstation niet in de lijst stations zit.
    while (str(eindstation) not in stations):
        # Vraag om een geldig eindstation
        eindstation = input("Dit is niet geldig, vul een geldig eindstation in: ");
    # Terwijl het ingevoerde eindstation WEL in de lijst stations zit.
    while str(eindstation) in stations:
        # Als de plek van de eindstation later is in de lijst stations dan het beginstation, geef de eindstation door.
        if stations.index(eindstation) > stations.index(begin):
            return eindstation;
        # Zo niet, vraag om een geldig eindstation na het beginstation in de lijst.
        else:
            eindstation = input("Dit is niet geldig, vul een eindstation na het beginstation in: ");

def omroepen_reis(begin, eind):
    #Sinds lists beginnen bij 0, geef ik de plek van het beginstation in de lijst + 1 zodat het bij 1 begint.
    print("Het beginstation " + begin + " is het " + str(stations.index(begin) + 1) + "e station in het traject");
    # Hetzelfde hier.
    print("Het eindstation " + eind + " is het " + str(stations.index(eind) + 1) + "e station in het traject");
    # Afstand is de plek van het beginstation in de lijst - de plek van het eindstation in de lijst.
    afstand = abs((stations.index(begin) + 1) - (stations.index(eind) + 1));

    print("De afstand bedraagt " + str(afstand) + " station(s)");

    prijs = afstand * 5;

    print("De prijs van het kaartje is " + str(prijs) + " euro.");

    print("Jij stapt in de trein in: " + str(begin));
    # Wat dit doet is dat het iets runt voor 1 tot afstand keer, dus als afstand 2 is 1 keer.
    for x in range(1, afstand):
        # Print uit het station dat op de plek van beginstation in de lijst + de stap waar we zijn.
        # Dus als hij voor de 2de keer dit runt, krijg je het station dat op de plek van het beginstation zit + 2.
        print("     - " + stations[stations.index(begin) + x]);

    print("Jij stapt uit in: " + str(eind));

begin = inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
omroepen_reis(begin, eind)