"""
Entrega 5: ejercicio 9
"""
class Coche:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
    def imprimir(self):
        print("Marca:", self.marca, "--- Modelo:", self.modelo)

car1=Coche("Ford", "Fiesta")
car2=Coche("Citröen","C5")

car1.imprimir()
car2.imprimir()