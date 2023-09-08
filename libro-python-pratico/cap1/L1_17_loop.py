print ("inserisci i valori dei tre lati di un triangolo")

x = int(input("Inserisci il valore del primo lato: "))

y = int(input("Inserisci il valore del secondo lato: "))

z = int(input("Inserisci il valore del terzo lato: "))

if x == y and y == z:
    print("Il triangolo è equilatero")
elif x != y and y != z and x != z:
    if (x + y) < z or (x + z) < y or (y + z) < x:
        print("Il triangolo è geometricamente sbagliato")
    else:
        print("Il triangolo è scaleno")
else:
    if (x + y) < z or (x + z) < y or (y + z) < x:
        print("Il triangolo è geometricamente sbagliato")
    else:
        print("Il triangolo è isoscele")