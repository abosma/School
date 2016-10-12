kaartnummers = [line.rstrip('\n') for line in open('Les4\kaartnummers.txt')]
nummers = [];

#Met len kan ik de lengte van mijn list zien, dat is ook automatisch het aantal regels
print("Deze file telt " + str(len(kaartnummers)) + " regels.");

for x in kaartnummers:
    #Hier splits ik weer nummers en naam
    kaartnummer,naam = x.split(",");
    #Deze voeg ik toe aan een ander list zodat ik het grootste nummer kan krijgen
    nummers.append(kaartnummer);

#Met de max() functie pak ik het grootste nummer in de lijst, en met de index() functie krijg ik de plaats in de lijst dat de max nummer staat.
#Ik doe + 1 omdat lijsten beginnen bij 0, de + 1 zorgt ervoor dat de juiste regel wordt weergeven.
print("Het grootste kaartnummer is: " + str(max(nummers)) + " en deze staat op regel " + str(nummers.index(max(nummers)) + 1));