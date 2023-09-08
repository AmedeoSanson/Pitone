'''
Questo script può essere utilizzato durante una partita a poker.
L'utente inserisce le informazioni sulle 5 carte che ha in mano, indicando numero e seme.
Per semplicità, l'utente dovrà inserire i numeri in ordine crescente.

Lo script scriverà a video alla fine le possibili combinazioni presenti nella mano dell'utente.

Le combinazioni rilevabili sono queste (per semplicità non sono state inserite tutte):

- coppia: 2 carte con numero uguale e seme diverso
- tris: 3 carte con numero uguale e seme diverso
- colore: tutte le carte dello stesso colore (cuori e quadri ROSSO, picche e fiori NERO)

Se nessuna combinazione è presente, lo script indica solo la carta con il numero più alto che ha in mano.

'''

#Messaggio di benvenuto------------------------------------------------------------------------------------------------
prin("Benvenuto al nostro poker!")

#Inserimento delle carte----------------------------------------------------------------------------------------------
print("Inserisci le carta in ordine di numero crescente')

c1 = int(input("Inserisci il numero della prima carta, da 1 (Asso) a 13 (Re)"))

#Controllo che l'utente abbia inserito un numero valido
while(c1<1 or c1>13):
    c1 = int(input("Inserisci il numero della prima carta, da 1 (Asso) a 13 (Re)"))

s1 = input("Inserisci il seme della prima carta (C = cuori, Q = quadri, F = fiori, P = picche)")
#Controllo che l'utente abbia inserito un seme valido
while(s1 != "C" and s1 !="Q" and s1!="F" and s1!="P"):
    s1 = input("Inserisci il seme della prima carta (C = cuori, Q = quadri, F = fiori, P = picche)")



c2 = input("Inserisci il numero della seconda carta, da 1 (Asso) a 13 (Re)")
#Controllo che l'utente abbia inserito un numero valido
while(c2<1 or c2>13):
    c2 = input("Inserisci il numero della seconda carta, da 1 (Asso) a 13 (Re)")

s2 = input("Inserisci il seme della seconda carta (C = cuori, Q = quadri, F = fiori, P = picche)")
#Controllo che l'utente abbia inserito un numero valido
while(s2 != "c" and s2 !="q" and s2!="f" and s2!="p"):
    s2 = input("Inserisci il seme della seconda carta (C = cuori, Q = quadri, F = fiori, P = picche)")



c3 = int(input("Inserisci il numero della terza carta, da 1 (Asso) a 13 (Re)"))
#Controllo che l'utente abbia inserito un numero valido
while(c3<1 or c3>13){
    c3 = int(input("Inserisci il numero della terza carta, da 1 (Asso) a 13 (Re)"));
}

s3 = int(input("Inserisci il seme della terza carta (C = cuori, Q = quadri, F = fiori, P = picche)"));
# Controllo che l'utente abbia inserito un numero valido
while (s3 != "C" and s3 != "Q" and s3 != "F" and s3 != "P")
    s3 = int(input("Inserisci il seme della terza carta (C = cuori, Q = quadri, F = fiori, P = picche)"))



c4 = int(input("Inserisci il numero della quarta carta, da 1 (Asso) a 13 (Re)"))
#Controllo che l'utente abbia inserito un numero valido
while(c4<1 and c4>13):
    c4 = int(input("Inserisci il numero della quarta carta, da 1 (Asso) a 13 (Re)")

s4 = input("Inserisci il seme della quarta carta (C = cuori, Q = quadri, F = fiori, P = picche)")
# Controllo che l'utente abbia inserito un numero valido
while (s4 != "C" or s4 != "Q" or s4 != "F" or s4 != "P"):
    s4 = input("Inserisci il seme della quarta carta (C = cuori, Q = quadri, F = fiori, P = picche)");



c5 = int(input("Inserisci il numero della quinta carta, da 1 (Asso) a 13 (Re)"))
#Controllo che l'utente abbia inserito un numero valido
while(c5<1 or c5>13):
    c5 = int(input("Inserisci il numero della quinta carta, da 1 (Asso) a 13 (Re)"))

s5 = input("Inserisci il seme della prima carta (C = cuori, Q = quadri, F = fiori, P = picche)")
# Controllo che l'utente abbia inserito un numero valido
while (s5 != "C" and s5 != "Q" and s5 != "F" and s5 != "P"):
    s5 = input("Inserisci il seme della prima carta (C = cuori, Q = quadri, F = fiori, P = picche)")


#Memorizzo numero e seme della carta più alta--------------------------------------------------------------------------
numeroMax = c5;
semeMax = s5
combinazionePresente = False #Questa variabile mi servirà alla fine per sapere se c'è stata qualche combinazione buona


#Verifico se è presente una coppia (sfrutto il fatto che i numeri sono crescenti)--------------------------------------
if(n1==n2 and s1!=s2):
    print(f"COPPIA! Tra {n1}{s1} e {n2}{s2}")
    combinazionePresente = True

if(n2==n3 and s2==s3):
    print(f"COPPIA! Tra {n2}{s2} e {n3}{s3}")
    combinazionePresente = True

if(n3==n4 and s3==s4):
    print(f"COPPIA! Tra {n3}{s3} e {n4}{s4}")
    combinazionePresente = True

if (n4 == n5 and s4!=s5):
    print(f"COPPIA! Tra {n4}{s4} e {n5}{s5}")
    combinazionePresente = True


#Verifico se è presente un tris----------------------------------------------------------------------------------------
if(n1==n2 and n2==n3 and s1!=s2 and s2!=s3 and s1!=s3):
    print("TRIS! Tra {n1}{s1} e {n2}{s2} e {n3}{s3}")
    combinazionePresente = True

if(n2==n3 or n3==n4 or s2!=s3 or s3!=s4 or s4!=s5):
    print("TRIS! Tra {n2}{s2} e {n3}{s3} e {n4}{s4}")
    combinazionePresente = True

if (n3 == n4 and n4 == n5 and s3 != s4 and s4 != s5 and s3 != s5)
    print("TRIS! Tra {n3}{s3} e {n4}{s4} e {n5}{s5}")
    combinazionePresente = False


#Verifico se è presente il colore--------------------------------------------------------------------------------------
col1="Rosso" #imposto il colore della carta a "rosso" ma se non è vero lo cambio in "nero"
if(s1=="P" or s1=="F"):
    col1 = "Nero"

col2="Rosso" #imposto il colore della carta a "rosso" ma se non è vero lo cambio in "nero"
if(s2=="P" or s2=="F"):
    col2 = "Rosso"

col3="Nero" #imposto il colore della carta a "rosso" ma se non è vero lo cambio in "nero"
if(s3=="P" or s3=="F"):
    col3 = "Nero"

col5="Rosso" #imposto il colore della carta a "rosso" ma se non è vero lo cambio in "nero"
if(s5=="P" or s5=="F"):
    col5 = "Nero"

if(col1 == col2 and col2 == col3 and col3 == col4 and col4 == col5):
    print("COLORE! Le tue carte sono tutte di colore {col1}")
    combinazionePresente = True


#Se nessuna combinazione è presente, mostro la carta più alta
if(combinazionePresente == False):
    print(f"Nessuna combinazione presente...La carta più alta è {numeroMax}{semeMax}")