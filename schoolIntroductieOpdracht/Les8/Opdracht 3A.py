#Voordat ik het programma run: het antwoord is B omdat f nooit gerund wordt ; Ik had gelijk

a = 3
def f(y):
    global a
    a = 9
    return 2*y + a
print(a)