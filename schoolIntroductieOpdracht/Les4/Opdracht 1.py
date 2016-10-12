def convert(CEL):
    #Gooi een nummer erin en deze wordt geconverteerd en gereturnd als FAH
    FAH = CEL * 1.8 + 32;
    return FAH;

def table():
    print("   F     C   ");
    #deze for loop gaat dus van -30 tot 40, maar in stappen van 10
    for x in range(-30,40,10):
        #x is dus altijd de celcius die je nodig hebt, dus kun je deze makkelijk gebruiken met de convert functie
        print(str(convert(x)) + "    " + str(x));

table();
