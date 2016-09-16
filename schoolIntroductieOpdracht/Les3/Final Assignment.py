aantalKMnodig = input("Wat is het aantal KM dat gereist moet worden?: ");
leeftijd = input("Wat is uw leeftijd?: ");
ishetweekend = input("Is het het weekend?: ");


def standaardprijs(afstandKM):
    if int(afstandKM) <= 0:
        afstandKM = 0;
        print("Het aantal kilometer is nu 0");
        return 0;
    if int(afstandKM) <= 15:
        prijs = afstandKM * 0.8;
        return prijs;
    else:
        prijs = 15 + (afstandKM * 0.6);
        return prijs;

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        prijs = standaardprijs(afstandKM) * 0.7;
        return prijs;
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        prijs = standaardprijs(afstandKM) * 0.65;
        return prijs;
    if leeftijd > 12 or leeftijd < 65 and weekendrit == False:
        prijs = standaardprijs(afstandKM);
        return prijs;
    if leeftijd > 12 or leeftijd < 65 and weekendrit == True:
        prijs = standaardprijs(afstandKM) * 0.6;
        return prijs;

def str2bool(jaofnee):
    if jaofnee == "Ja":
        return True;
    if jaofnee == "Nee":
        return False;

ishetweekend = str2bool(ishetweekend);

eindprijs = ritprijs(int(leeftijd),ishetweekend,int(aantalKMnodig));

print("Het prijs dat u moet betalen is: " + str(eindprijs) + " euro.");