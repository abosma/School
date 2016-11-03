#Ik snapte de opdracht niet dus zal ik dit later vragen
bruin = {"best","beukenlaan","helmond 't hout","helmond","helmond brouwhuis","deurne"}
groen = {"best","beukenlaan","geldrop","heeze","weert"}
print("De volgende stations komen in beide trajecten voor:" + bruin.intersection(groen))
print("Deze stations verschillen met het groene traject:" + bruin.difference(groen))
print("Dit zijn alle stations:" + groen.union(bruin))