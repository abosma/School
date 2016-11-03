import csv
import random


def optieMenu(keuze):
    while keuze > 5 or keuze < 1:
        print("Dit is geen optie")
        print("1: Ik wil een nieuwe kluis\n" + 
              "2: Ik wil mijn kluis openen\n" + 
              "3: Ik geef mijn kluis terug\n" + 
              "4: Ik wil weten hoeveel kluizen nog vrij zijn\n" + 
              "5: Ik wil stoppen\n")
        keuze = int(input("Kies een van de bovenstaande opties: "))
    if keuze == 1:
        nieuwe_kluis()
    if keuze == 2:
        kluis_openen()
    if keuze == 3:
        kluis_teruggeven()
    if keuze == 4:
        aantal_kluizen_vrij()
    if keuze == 5:
        print("Quitting program")


def nieuwe_kluis():
    code = 0

    while code < 1000 or code == 10000:
        code = int(10000 * random.random())

    with open("Les7/kluizen.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        kluisDict = {}
        for row in reader:
            kluisDict[row[0].strip("\t")] = row[1].strip("\t");

    with open("Les7/kluizen.csv", "r") as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=";")
        vrijeKluis = []
        volleKluis = []
        for row in reader:
            if row[1] == "":
                vrijeKluis.append(row[0])
            else:
                volleKluis.append(row[0])

    if vrijeKluis == []:
        print("Er zijn geen kluizen beschikbaar");

    else:
        print("Kluis " + vrijeKluis[0] + "is beschikbaar");
        print("Jouw code is " + str(code));

    if vrijeKluis != []:
        with open("Les7/kluizen.csv", "w", newline="") as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter=";")

            kluisDict[vrijeKluis[0]] = code

            for key, value in kluisDict.items():
                writer.writerow([key, value])


def kluis_openen():
    code = input("Voer uw code in: ")
    incorrecteCode = 0
    with open("Les7/kluizen.csv", "r") as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=";")
        for row in reader:
            if row[1] == code:
                print("Kluis", row[0], "is geopend")
            else:
                incorrecteCode = incorrecteCode + 1
    if incorrecteCode == 13:
        print("Code onjuist")


def kluis_teruggeven():
    print("Deze optie is niet gemaakt sinds het optioneel is, probeer een andere keuze: \n" +
            "1: Ik wil een nieuwe kluis\n" + 
            "2: Ik wil mijn kluis openen\n" + 
            "3: Ik geef mijn kluis terug\n" + 
            "4: Ik wil weten hoeveel kluizen nog vrij zijn\n" + 
            "5: Ik wil stoppen\n")

    keuze = int(input("Kies een van de bovenstaande opties: "))

    optieMenu(keuze)


def aantal_kluizen_vrij():
    with open("Les7/kluizen.csv", "r") as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=";")
        y = 0
        for row in reader:
            if row[1] == "":
                y = y + 1
    print("Aantal vrije kluisjes is:" + y)



print("1: Ik wil een nieuwe kluis\n" + 
              "2: Ik wil mijn kluis openen\n" + 
              "3: Ik geef mijn kluis terug\n" + 
              "4: Ik wil weten hoeveel kluizen nog vrij zijn\n" + 
              "5: Ik wil stoppen\n")

keuze = int(input("Kies een van de bovenstaande opties: "))

optieMenu(keuze)
