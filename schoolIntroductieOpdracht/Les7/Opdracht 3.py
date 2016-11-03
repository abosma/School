import csv

with open("Les7/scoreFile.csv", "r") as csvfile:
    csvReader = csv.reader(csvfile);
    cijferLijst = []
    volleLijst = []
    for row in csvReader:
        for x in row:
            lists = x.split(";")
            cijferLijst.append(lists[2]);
            volleLijst.append(lists);
    
    for x in volleLijst:
        for y in x:
            try:
                max_index = x.index(max(cijferLijst))
                if x[max_index]:
                    print("De hoogste score is: " + x[2] + " op " + x[1] + " behaald door " + x[0])
                    break;
            except Exception as e:
                continue;