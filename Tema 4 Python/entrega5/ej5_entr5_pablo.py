"""
Entrega 5: ejercicio 5
Programa realizado por Pablo Blázquez Sánchez
Este programa muestra los números dentro de un intervalo por defecto, luego
entre otro intervalo que no es por defecto, un intervalo desde un número
"""
def contador(a=20,b=30):
    for x in range(a,b):
        print(x)

contador()
contador(2)
contador(12,34)