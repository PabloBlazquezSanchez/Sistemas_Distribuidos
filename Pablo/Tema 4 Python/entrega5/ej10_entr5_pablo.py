"""
Entrega 5: ejercicio 10
"""
class Coche:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
    
    def imprimir(self):
        print("Marca:", self.marca, "--- Modelo:", self.modelo)

class Todoterreno(Coche):
    pass

coche1=Todoterreno("Citröen", "C4")
coche2=Todoterreno("Toyota", "Auris")

coche1.imprimir()
coche2.imprimir()