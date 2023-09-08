fine = False
p1=p2=p3=p4=p5=p6=p7=p8=p9="-"

turno = "X"

while not fine:
    print("\n\n")
    print(f"Tocca a {turno}: scegli una posizione")
    print("1 | 2 | 3")
    print("----------")
    print("4 | 5 | 6")
    print("----------")
    print("7 | 8 | 9")

    print("\n\n")

    print(f"{p1} | {p2} | {p3}")
    print("----------")
    print(f"{p4} | {p5} | {p6}")
    print("----------")
    print(f"{p7} | {p8} | {p9}")

    posizione = int(input())

    if(posizione == 1 and p1=="-"):
        p1=turno
    elif (posizione == 2 and p2=="-"):
        p2=turno
    elif (posizione == 3 and p3=="-"):
        p3=turno
    elif (posizione == 4 and p4=="-"):
        p4=turno
    elif (posizione == 5 and p5=="-"):
        p5=turno
    elif (posizione == 6 and p6=="-"):
        p6=turno
    elif (posizione == 7 and p7=="-"):
        p7=turno
    elif (posizione == 8 and p8=="-"):
        p8=turno
    elif (posizione == 9 and p9=="-"):
        p9=turno
    else:
        print("Scelta sbagliata")
        continue
    
    print("Campo aggiornato:")
    print(f"{p1} | {p2} | {p3}")
    print("----------")
    print(f"{p4} | {p5} | {p6}")
    print("----------")
    print(f"{p7} | {p8} | {p9}")
    
    if((p1==p2==p3 and p1!="-") or (p4==p5==p6 and p4!="-") or (p7==p8==p9  and p7!="-") or (p1==p4==p7 and p1!="-") or (p2==p5==p8 and p2!="-") or (p3==p6==p9 and p3!="-") or (p1==p5==p9 and p1!="-") or (p3==p5==p7 and p3!="-")):
        print(f"\n\nIl giocatore {turno} ha vinto!")
        fine = True

    if(p1!="-" and p2!="-" and p3!="-" and p4!="-" and p5!="-" and p6!="-" and p7!="-" and p8!="-" and p9!="-"):
        print("Il gioco è terminato in parità")
        fine = True

    if(turno=="X"):
        turno="O"
    else:
        turno="X"

    _ = input("Premi un tasto per continuare")

print("FINE DEL GIOCO!")5