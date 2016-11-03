import csv

with open("Les7/artikelFile.csv", 'w', newline='\n') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(["Artikelnummer"] + ["Artikelcode"] + ["Naam"] + ["Voorraad"] + ["Prijs"])
    csvwriter.writerow(["123"] + ["ABC123"] + ["Highlight pen"] + ["231"] + ["0.56"])
    csvwriter.writerow(["123"] + ["PQR678"] + ["Nietmachine"] + ["587"] + ["9.99"])
    csvwriter.writerow(["128"] + ["ZYX163"] + ["Bureaulamp"] + ["34"] + ["19.95"])
    csvwriter.writerow(["137"] + ["MLK709"] + ["Monitorstandaard"] + ["66"] + ["32.50"])
    csvwriter.writerow(["271"] + ["TRS665"] + ["Ipad hoes"] + ["155"] + ["19.01"])

with open("Les7/artikelFile.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(csvfile)
        artikelList = []
        for row in reader:
            artikelList.append(row);

        prijzenLijst = []
        for y in artikelList:
            prijzenLijst.append(y[4])
       
        for x in artikelList:     
            try:
                max_index = x.index(max(prijzenLijst, key=float))
                totaalVoorraad = 0;

                for artikels in artikelList:
                    voorraadNummer = int(artikels[3])
                    totaalVoorraad += voorraadNummer;

                if x[max_index]:
                    print("Het duurste artikel is " + x[2] + " en die kost " + x[4] + " Euro\n" +
                            "Er zijn slechts " + x[3] + " exemplaren in voorraad van het product " + x[1] + " met nummer " + x[0] + "\n" +
                            "In totaal hebben wij " + str(totaalVoorraad) + " producten in ons magazijn liggen")
                    break;
            except Exception as e:
                continue;
