from dispositivoIoT import DispositivoIoT

class LampoIot(DispositivoIoT):
    def __init__(self,nome):
        super().__init__(nome)
        self.colore="bianco"
        self.intensita=0

    def __repr__(self):
        return f"lampada: {super().__repr__()} colore: {self.colore} intensità: {self.intensita}"

    def impostaValore(self, valore):#vaore è un dizionario accedo ad i suoi valori con le quadre e apici
        self.colore=valore['colore']
        self.intensita=valore['intensita']

'''
lamp1= LampoIot("lampidina")
lamp1.impostaValore({'colore':input("dammi un colore"),'intensita':int(input("quanto acceso"))})

print(lamp1)'''