class Punto2D:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y

    def __repr__(self):
        return f"(X:{self.X},Y:{self.Y})"

    def calcolaNorma(self):# calcolo la distanza dal centro
        c=(self.X)**2+ (self.Y)**2
        return round(c**0.5,2)

    def calcolaDistanza(self,puntoB):#calcola la distanza dal punto B
        c=(self.X-puntoB.X)**2 + (self.Y-puntoB.Y)**2
        return round(c**0.5,2)
'''
puntoA=Punto2D(int(input("dammi la X: ")),int(input("dammi la Y: ")))

print(puntoA.calcolaNorma())
secondo=Punto2D(int(input("dammi una seconda X: ")),int(input("dammi una seconda Y: ")))
print(puntoA.calcolaDistanza(secondo))
'''