from dispositivoIoT import DispositivoIoT

class TermosIoT(DispositivoIoT):
    def __init__(self,nome):
        super().__init__(nome)
        self.temp=0

    def __repr__(self):
        return f"la temperatura impostata è: {self.temp}"

    def impostaValore(self, valore):
        self.temp=valore['temp']
'''
termos1=TermosIoT("giggino")
termos1.impostaValore({'temp':int(input("quanti gradi vuoi: "))})

print(f"hai impostato: {termos1.temp}")
#print(termos1.temp)
'''
