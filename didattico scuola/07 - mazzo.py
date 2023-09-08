class Mazzo:

    def __init__(self, tipo="briscola"):
        if(tipo == "briscola"):
            valori = [ i for i in range(1,11) ]
            semi = ["D", "S", "B", "C"]
        else:
            valori = [i for i in range(1, 14)]
            semi = ["P", "F", "Q", "C"]

        self.carte = [(v, s) for v in valori for s in semi]

    def __repr__(self):
        return f"Mazzo:\n{self.carte}"

    #Restituisce il numero di carte nel mazzo
    def cartePresenti(self):
        return len(self.carte)

    def guardaPrimaCarta(self):
        return self.carte[0]

    def estraiCarta(self):
        return self.carte.pop(0)

    def inserisciCarta(self, nuovaCarta):
        if(nuovaCarta not in self.carte):
            self.carte.append(nuovaCarta)

briscola = Mazzo()
poker = Mazzo("poker")

_ = briscola.estraiCarta()
nuovaCartaB = (1,"D")
briscola.inserisciCarta(nuovaCartaB)
print(briscola.cartePresenti())

nuovaCartaP = (1, "P")
poker.inserisciCarta(nuovaCartaP)
print(poker.cartePresenti())