annuleringen = [line.rstrip('\n') for line in open('Les4\Annuleringen.txt')]

annuleringen = [w.replace('Annulering: ','') for w in annuleringen];

treinritten = [line.rstrip('\n') for line in open('Les4\Treinritten.txt')]

for i in annuleringen:
    for y in treinritten:
        if i in y:
            treinritten.remove(y);

print('\n'.join(treinritten));