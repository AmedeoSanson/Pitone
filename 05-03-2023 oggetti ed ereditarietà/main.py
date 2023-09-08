class persona:
    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta

    def __repr__(self):
        return f"{self.nome} - {self.cognome} - {self.eta}"

class studente (persona):
    def __init__(self,h,g,e,classe):
        super().__init__(h,g,e)
        self.classe=classe

    def __repr__(self):
        return f"{super().__repr__()} - {self.classe}"

class insegnate (persona):
    def __init__(self,nome,cognome,eta,materia,classi):
        super().__init__(nome,cognome,eta)
        self.materia=materia
        self.classi=classi

    def __repr__(self):
        return f"{super().__repr__()} - {self.classi} - {self.materia}"

class segretario (persona):
    pass

studente1=studente(input("nome studente: "),input("cognome: "),int(input("età: ")),input("classe: "))

print(studente1)

nardin=insegnate("paride","nardin",40,"plc",["1-smart","2-smart","1-mecc"])

print(nardin)