"""
Entrega 5: ejercicio 12
Programa realizado por Pablo Blázquez Sánchez
Programa que suma dos números mediante un módulo
"""
import operacionespablo

print("Vamos a sumar dos números mediante una función suma importada de un módulo")

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

print("La suma es:", operacionespablo.Suma(num1, num2))