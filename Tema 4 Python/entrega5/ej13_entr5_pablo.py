"""
Entrega 5: ejercicio 13
Programa realizado por Pablo Blázquez Sánchez
"""

from operacionespablo import Producto

print("Vamos a multiplicar dos números mediante una función producto importada de un módulo")

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

resultado = Producto(num1, num2)

print("El producto es:", resultado)