dict = {"student1":70, "student2":65, "student3":55, "student4":40, "student5":91, "student6":85, "student7":80, "student8":95};

print ("Alle studenten boven een 90\n");

# Voor ieder 2 items in de dictionary
for naam, nummer in dict.items():
    # Als het 2de item meer dan 90 is.
    if nummer >= 90:
        # Print de eerste en tweede item uit.
        print ("Naam: " + naam + " - Nummer: " + str(nummer));