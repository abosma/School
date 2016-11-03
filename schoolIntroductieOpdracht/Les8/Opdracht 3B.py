#Voordat ik het programma run: het antwoord is D omdat x nooit wordt geprint en omdat met global y y wordt verandert naar 3 ; Ik had gelijk

x = 1
y = 4
def fun():
     x = 2
     global y
     y = 3
     print(y, end = ' ')
fun()
print(y, end = ' ')