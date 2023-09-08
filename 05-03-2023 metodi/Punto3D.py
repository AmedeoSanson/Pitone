from Punto2D import Punto2D

class Punto3D(Punto2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

    def __repr__(self):
        return f"x: {super().X} - y: {super().Y} - z: {self.z}"

    def calcolaNormaZ(self):
        c= super().calcolaNorma()**2+self.z**2
        return round(c**0.5,2)

    def calcolaDistanz(self,puntoB):
        c= super().calcolaDistanza()**2 + puntoB.z**2
        return round(c^0.5,2)

puntoAZ = Punto3D(int(input("dammi na X: ")),int(input("dammi una Y: ")),int(input("dammi una Z: ")))
puntoBZ = Punto3D(int(input("dammi na X: ")),int(input("dammi una Y: ")),int(input("dammi una Z: ")))
print(puntoAZ.calcolaNormaZ())
print(puntoAZ.calcolaDistanz(puntoBZ))