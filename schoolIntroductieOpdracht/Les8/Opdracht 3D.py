#Voordat ik het programma run: het antwoord is C ; Ik had het goed

a = 3
def fun1():
    global a
    print("a:", a, end = ' ')
    b = 7
    a = 0
    return b

def fun2(y):
    a = y + fun1()
    b = 7
    a += 1
    return a
a = 9
fun2(5)
print("a:", a)