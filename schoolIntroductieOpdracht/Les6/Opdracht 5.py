import random

    
def monopolyworp():
    loop = 1;
    dubbel = 0;
    #Ik gebruik weer een infinite loop om iedere keer nieuwe random nummers te krijgen
    while loop == 1:
        #Hier gebruik ik de randomint functie om een nummer tussen 0 en 7 te krijgen
        rand1 = random.randint(1,6);
        rand2 = random.randint(1,6);
        #Als rand1 en rand2 niet hetzelfde zijn
        if rand1 != rand2:
            #Print gewoon de resultaat uit en break de loop
            print(str(rand1) + " + " + str(rand2) + " = " + str((rand1 + rand2)));
            break;
        #Als het wel hetzelfde is en dubbel niet 3 is
        elif rand1 == rand2 and dubbel != 3:
            #Doe + 1 bij de dubbel var
            dubbel += 1;
            #En print de resultaat uit, omdat er geen break staat gaat ie weer terug naar het begin en krijg je weer nieuwe nummers
            print(str(rand1) + " + " + str(rand2) + " = " + str((rand1 + rand2)) + " (dubbel)");
        #Als het nummer hetzelfde is en dubbel wel 3 is
        elif rand1 == rand2 and dubbel == 3:
            #Print dat ie naar de gevangenis moet en break de loop om de functie te eindigen
            print(str(rand1) + " + " + str(rand2) + " = " + "direct naar de gevangenis.");
            break;


monopolyworp();