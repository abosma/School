studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    # Maak eerst een lege lijst waar de cijfers in kunnen.
    antw = [];
    # Voor iedere lijst in de lijst.
    for list in studentencijfers:
        # som is de som van de lijst in de lijst
        som = sum(list);
        # Gemiddelde
        gemiddelde = som / len(list);
        # De gemiddelde wordt in de nieuwe lijst gezet, en gaat door naar de volgende lijst in de lijst tot er geen lijsten meer zijn.
        antw.append(gemiddelde);
    return antw; 

def gemiddelde_van_alle_studenten(studentencijfers):
    # Maak een lege lijst.
    lijst = [];
    #Voor iedere lijst in de lijst.
    for list in studentencijfers:
        #Voor iedere nummer in de lijst.
        for x in list:
            # Doe iedere nummer in de lege lijst
            lijst.append(x);
            # Doe al deze nummers bij elkaar.
            som = sum(lijst);
            # Bereken het gemiddelde
            gemiddelde = som / len(lijst);
            # De return wordt nu de gemiddelde van alle nummers.
            antw = gemiddelde;
    return antw;

print(str(gemiddelde_per_student(studentencijfers)));
print(str(gemiddelde_van_alle_studenten(studentencijfers)));