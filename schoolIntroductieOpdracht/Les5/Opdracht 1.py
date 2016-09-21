a = int(input("Wat is het huidge maandnummer?"));

def seizoen(maand):
    maandNaam = "";
    #als de ingevoerde maand 3 of meer is, en 5 of minder geef de string maandNaam met de value Lente terug.
    if maand >= 3 and maand <= 5:
        maandNaam = "Lente";
        return maandNaam;
    #als de ingevoerde maand 9 of meer is, en 511 of minder geef de string maandNaam met de value Herfst terug.
    elif maand >= 9 and maand <= 11:
        maandNaam = "Herfst";
        return maandNaam;
    #als de ingevoerde maand 6 of meer is, en 8 of minder geef de string maandNaam met de value Zomer terug.
    elif maand >= 6 and maand <= 8:
        maandNaam = "Zomer";
        return maandNaam;
    #als de ingevoerde maand 11 of meer is, en 3 of minder geef de string maandNaam met de value Winter terug.
    elif maand >= 11 or maand <= 3:
        # Het probleem is dat als deze meer dan 12 was of minder dan 1, gaf dit ook Winter terug,
        # Daarom bestaat deze if statement om zeker te weten dat de ingevoerde nummer hoger dan 0 en lager dan 13 is.
        if maand > 12 or maand < 1:
            maandNaam = "Er zijn maar 12 maanden en 0 of een mingetal is geen maand...";
            return maandNaam;
        maandNaam = "Winter";
        return maandNaam;
    # Als er geen nummer is ingevoerd geef dit terug.
    else:
        maandMaan = "Er is geen nummer ingevuld, probeer nog een keer.";

print(seizoen(a));