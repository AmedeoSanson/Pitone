so=1
while so==1:
    print("Scegli una voce:\n1)Scrivi ciao\n2)Somma\n3)Estrai\n4)muoio")

    a=int(input("scegli cosa vuoi che faccia\n"))
    match a:
        case 1:
            print("ciao bro\n")
        case 2:
            print("scrivi due numeri e io ti farò la somma")
            som1=int(input("primo number: "))
            som2=int(input("secondo number: "))
            print(som1+som2)
        case 3:
            print("dammi una stringa ed io taglierò inizio e fine\n")
            string1=input()
            print(string1[1:-1])#mi taglia il primo e l'ultimo carattere della stringa
        case 4:
            print("mi suicido")
            so=0
        case _:
            print("brutto pezzo di merda che cazzo vuoi fare\nsei per caso cieco?\nrincoglionito?")