#Zet de regels in een list
kaartnummers = [line.rstrip('\n') for line in open('Les4\kaartnummers.txt')]

#Voor iedere regel
for x in kaartnummers:
    #De regel wordt gesplitst bij de , ,dus op deze manier kun je de naam een kaartnummer ieder hun eigen string geven
    kaartnummer,naam = x.split(",");
    #En hier print ik hem gewoon uit
    print(naam + " heeft kaartnummer: " + kaartnummer);