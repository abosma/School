#voor een while loop heb je een basis getal nodig, daarom is er hier eerst een input variable.
#de b = 1 is gedaan omdat de eerste input niet in de while loop zit, dus wordt deze niet meegeteld.
#list = [a] is gedaan om de eerste input in de lijst te zetten voor de sum.
a = eval(input("Geef een getal: "));
b = 1;
list = [a];

#terwijl de input niet 0 is, vraagt het iedere keer weer om een nieuw input.
#b wordt ook iedere keer hoger voor ieder getal ingevoerd met b = b + 1.
#voor de som van alle getallen wordt ieder ingevoerd getal ook 
while a != 0:
    a = eval(input("Geef een getal: "));
    b = b + 1;
    list.append(a);


print("Er zijn " + str(b) + " getallen ingevoerd, de som is: " + str(sum(list)));