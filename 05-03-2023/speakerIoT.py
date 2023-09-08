from dispositivoIoT import DispositivoIoT

class SpeakerIot (DispositivoIoT):
    def __init__(self,nome):
        super().__init__(nome)
        self.canzone=""
        self.volume=0

    def __repr__(self):
        return f"speaker: {super().__repr__()}, canzone: {self.canzone}, volume: {self.volume}"

    def impostaValore(self, valore):
        self.canzone=valore['canzone']
        self.volume=valore['volume']

'''
speaker1=SpeakerIot("giggino")
speaker1.impostaValore({'canzone':input("canzone:"),'volume':int(input("volume: "))})

print(f"hai impostato: {speaker1}")
#print(speaker1)
'''