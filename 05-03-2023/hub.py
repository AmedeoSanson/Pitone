from dispositivoIoT import DispositivoIoT
from lampoIoT import LampoIot
from termosIoT import TermosIoT
from speakerIoT import SpeakerIot

class Hub(DispositivoIoT):
    def __init__(self,nome,listaDispositivi):
        super().__init__(nome)
        self.ListaDispositivi=[]

        for d in listaDispositivi:
            self.aggiungiDispositivo(d)

    def __repr__(self):
        return f"hub: {super().__repr__()}, lista dispositivi: {self.ListaDispositivi}"

    def aggiungiDispositivo(self,nuovoDisp):
        if(isinstance(nuovoDisp,DispositivoIoT)):
            self.ListaDispositivi.append(nuovoDisp)

h= Hub("buddy",[])

lam1= LampoIot("lampione")
lam2= LampoIot("Lampino")

speaker1= SpeakerIot("cassa centrale")

speaker1.impostaValore({'canzone':"gigi di alesio",'volume':69})
h.aggiungiDispositivo(lam1)
h.aggiungiDispositivo(lam2)
h.aggiungiDispositivo(speaker1)
h.aggiungiDispositivo("gigino")

print(h)