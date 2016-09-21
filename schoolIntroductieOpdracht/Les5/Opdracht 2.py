list = eval(input("Geef lijst met minimaal 10 strings: "));
list2 = [];

#voor iedere element in de lijst, check of dit element 4 letters of minder is.
#als deze 4 of minder lang is, doe deze in lijst 2.
for x in list:
    if len(x) <= 4:
        list2.append(x);

print(list2);