import random


class DispositivoIoT:
    def __init__(self, nome):
        self.nome = nome
        self.numeroSerie = random.randint(100, 100000)

    def __repr__(self):
        return self.nome

    def impostaValore(self, valore):
        return "da implementare"
