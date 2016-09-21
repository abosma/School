import math;

invoer = "5-9-7-1-7-8-3-2-4-8-7-9";
lijst = [];

#voor iedere letter in string invoer, check of het een nummer is. zo ja doe het in de lijst.
for x in invoer:
    if x.isdigit():
        lijst.append(x);

#list sorteren, key=int wordt gedaan zodat de list.sort weet dat het nummers zijn en dus een nummer sort doet en niet een string sort.
lijst.sort(key=int);
print("Gesorteerde list van ints: " + str(lijst));

#max pakt het grootste value in een list, en min de kleinste value.
print("Grootste getal: " + str(max(lijst)) + " en kleinste getal: " + str(min(lijst)));

#met de map functie kun je van een string list naar int list gaan, voor de sum functie moet je een int list hebben en daarom moest ik de map functie gebruiken hiervoor.
intList = list(map(int, lijst))
print("Aantal getallen: " + str(len(intList)) + " en Som van getallen: " + str(sum(intList)));

#gemiddelde wordt berekend door som / aantal getallen, dus de 2 eerder berekende variabelen. Dit allemaal in een print zetten is niet slim en het is beter om deze hun eigen variable te geven.
print("Gemiddelde: " + str((sum(intList) / len(intList))));
