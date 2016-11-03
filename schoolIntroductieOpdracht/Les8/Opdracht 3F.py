#Voordat ik het programma uitvoer: het antwoord is D ; Ik had het goed

a = 5
def fun1():
    global a
    b = 2
    a = 4
    return a+b
def fun2(y):
    global a
    a = y + fun1()
    a += 1
    return a
print("a:", a, end = ' ')
a = fun2(3)
print("a:", a)