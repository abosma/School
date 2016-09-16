leeftijd = input("Wat is jouw leeftijd: ");
paspoort = input("Heb je een nederlands paspoort: ");

if int(leeftijd) >= 18 and str(paspoort) == "Ja":
    print("Je mag stemmen!");
else:
    print("Je mag niet stemmen.");