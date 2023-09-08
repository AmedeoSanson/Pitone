import sys
class utente:
    def __init__(self,nomeUtente):

        self.nomeUtente=nomeUtente

    def __repr__(self):
        print(f"Nome Utente: {nomeUtente} ")

#utente1=utente(input("nome: "),input("cognome: "),input("password: "),input("nomeUtente: "))
utente1=utente(input("nomeUtente: "))
nomeUtenteProva=utente1.nomeUtente
if nomeUtenteProva.find("q")  :
    print("giusto\n")
else:
    print("sbagliato\n")
