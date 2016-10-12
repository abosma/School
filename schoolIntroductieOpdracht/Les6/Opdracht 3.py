def naam():
    loop = 1;
    naamDict = {}
    #Hier maak ik een infinite loop, op deze manier kan ik altijd de value a gebruiken in de loop en hoef ik deze niet eerder aan te maken
    while loop == 1:
        a = input("Volgende naam: ")
        #Als a niet leeg is
        if a != "":
            #Als er in de dictionary naamDict geen key met dezelfde naam als de input is
            if naamDict.get(a) is None:
                #Maak er een aan met de value van 1
                naamDict[a] = 1;
            else:
                #Als er wel een bestaat doe + 1 bij de value van deze key
                naamDict[a] += 1;
        #Als er niks is ingevuld
        else:
            #Deze for loop zorgt ervoor dat er key,value pairs zijn, dus x is key en y is value
            for x,y in naamDict.items():
                #Als de value dus 1 is
                if y == 1:
                    #Dan print ie de singulaire versie van deze zin uit
                    print("Er is " + str(y) + " student met de naam " + str(x));
                #Anders print ie de meerderheidsvorm van deze zin uit
                else:
                    print("Er zijn " + str(y) + " studenten met de naam " + str(x));
            #Dit zorgt ervoor dat de infinite loop gestopt wordt, anders is er dus een memory leak en kan het voor altijd doorgaan tot de computer crasht
            break;

naam();