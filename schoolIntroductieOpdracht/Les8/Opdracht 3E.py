#Voordat ik het programma uitvoer: het antwoord is C ; Ik had het goed

x = 1
y = 4
def doe1():
    global x
    y = 7
    x = 0
    return y
def doe2():
    x = doe1()
    x += 1
    return x
x = doe1()
print(x)