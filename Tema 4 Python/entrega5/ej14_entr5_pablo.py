"""
Entrega 5: ejercicio 14
Programa realizado por Pablo Blázquez Sánchez
"""

from operacionespablo import Cociente as dv

print("Vamos a dividir dos números mediante una función cociente importada de un módulo")
print("Esta función va a tener un apodo: \"dv\"")

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

resultado = dv(num1, num2)

print("El producto es:", resultado)