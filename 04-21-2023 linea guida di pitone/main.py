#il commento si con sta sta cosa
#in pitone le variabili non hanno una variabile predifinita,
#non ha le parentesi graffe, ne il ;
a = 0


#le variabili possono cambiare il tipo

a = "sooos"

print("Ciao a tutti broz",a," maaa")
b=2.34

print("oh fra",a,"ma ti dico anche",b)

eta=0
eta=  int(input("fra prova a darmi qualcosa: "))
#input trasforma tutto in stringa quindi per avere degli int fai
print("fra hai scritto",eta)

eta2=     int(input("dammi un altro nummero: "))

#se no avessi messo gli int prima degli input lui avrebbe scritto le due cose attaccate così invece fa la somma
print(eta+eta2)

#per le condizioni si if o altro dopo la condizione metto i ':' e le cose devo fare devo metterle con un tab

if eta>eta2:
    print("eta uno è maggiore di eta due")
elif eta==eta2:
    print("sono uguali")
else:
    print("eta2 è maggiore di eta uno")

#cicli while
#stapa i numeri da 0 a 10
i=0
while i<11:
    print(i)
    i+=1

#ciclo for
for i in range(o,11): #for(int i=0;i<11;i++)
    print(i)

# gli operatori logici si scrivono: and, or, not
