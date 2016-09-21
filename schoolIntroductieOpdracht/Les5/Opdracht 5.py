a = input("Geef een string van 4 letters: ");
print(a + " heeft " + str(len(a)) + " letters.");

#Terwijl lengte van input niet 4 is, ga door.
while len(a) != 4:
    a = input("Geef een string van 4 letters: ");
    print(a + " heeft " + str(len(a)) + " letters.");
    #Als de lengte van A 4 is, stop de loop met break en print welke string geslaagd is.
    if len(a) == 4:
        print("Inlezen van correcte string: " + a + " is geslaagd.");
        break;
