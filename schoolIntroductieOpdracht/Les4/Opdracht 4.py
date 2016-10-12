import pathlib
import time

#Met deze var kan ik een while loop maken van 5 keer, kon ook met een for loop met een range(0,5)
loop = 0;

while loop != 5:
    #Hier gebruik ik de library pathlib om te checken of de file bestaat
    file = pathlib.Path("Les4\Hardlopers.txt");

    #Hier vraag ik voor een naam
    a = input("Naam voor registratie: ");

    #Als de file bestaat
    if file.is_file():
        #Open de file met append en geef het de var naam textfile
        with open("Les4\Hardlopers.txt", "a") as textfile:
            #Schrijf in de textfile de tijd (de %a geeft de verkorte weekdagnaam en %d de dag van de maand van vandaag etc) plus de naam plus een newline character
            textfile.write(time.strftime("%a %d %b %Y, %T, ") + a + "\n");
    #Als deze niet bestaat
    else:
        #Maak een nieuwe aan met write (de "w") en schrijf hetzelfde als eerder
        textfile = open("Les4\Hardlopers.txt","w");
        textfile.write(time.strftime("%a %d %b %Y, %T, ") + a + "\n");
    #Aan het einde wanneer er iets is geschreven doe loop + 1, ander blijft de while loop maar doorgaan
    loop += 1;