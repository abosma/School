import math

def kwadraten_som(grondGetallen):
    r = grondGetallen[:]
    for idx,item in enumerate(grondGetallen):
        if item < 0:
           r.remove(item)
        else:
           r[idx] = math.pow(item,2);
    print(str(r));

a = [2,4,8,-10];

kwadraten_som(a);