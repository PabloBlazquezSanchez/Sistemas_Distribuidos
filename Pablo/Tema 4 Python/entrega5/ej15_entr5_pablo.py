"""
Entrega 5: ejercicio 15
Programa realizado por Pablo Blázquez Sánchez
Juego BUNCO reducido
"""
from random import randint
class Jugador():
    def tira(self):
        self.dado = []
        for x in range(3):
            self.dado.append(randint(1, 6))