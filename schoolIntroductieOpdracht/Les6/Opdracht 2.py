#Voor iedere lijn in open

def ticker(filename):
    tickerDict = {};
    for line in open(filename):
        #De value test is alles voor de newline
        test = line.rstrip("\n");
        #Split deze value voor en na de :
        test = test.split(":");
        #Test is nu een lijst met de volle naam op plaats 0, en de korte naam op plaats 1 bijv test[0] = YAHOO en test[1] is YHOO
        #Er wordt nu een nieuwe Key met de value test[0] gemaakt, met de value test[1] bijv 'YAHOO':'YHOO', 'inBev':'BUD'.
        tickerDict[test[0]] = test[1];
    return tickerDict;

a = input("Enter Company Name: ");

#.get() geeft de value voor de key dat je tussen de () invoer, dus als je YAHOO intypt zoekt hij in de dict voor de value van de key YAHOO
print(str(ticker("Les6\TickerFile.txt").get(str(a))));

b = input("Enter Ticker Symbol: ");

#Voor iedere item in de dictionary
for keys in ticker("Les6\TickerFile.txt"):
    #Als de ingevoerde ticker symbol hetzelfde is als de value van de huidige item (.get(keys) geeft me de value van de huidige item) 
    if b == ticker("Les6\TickerFile.txt").get(keys):
        #Print de key die hetzelfde value heeft als de ingevoerde text
        print(keys);