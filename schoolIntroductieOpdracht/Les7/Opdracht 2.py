import time
import csv

while True:
    try:
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            break;
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        with open("Les7\inloggers.csv", 'a', newline='\n') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';')
            csvwriter.writerow([time.strftime("%a %d %b %Y, %T")] + [voorl] + [naam] + [gbdatum] + [email])
    except Exception as e:
        print(e);
        break;