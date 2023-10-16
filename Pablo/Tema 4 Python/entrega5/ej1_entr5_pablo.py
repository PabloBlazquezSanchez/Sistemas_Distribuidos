"""
Entrega 5: ejercicio 1
Programa realizado por Pablo Blázquez Sánchez
Este programa suma dos números, introducidos por el usuario, mediante una función
"""
num1 = eval(input("Introduzca a continuación el primer número: "))
num2 = eval(input("Introduzca a continuación el segundo número: "))
def suma(a,b):
    return a + b
print("El resultado de su suma es:", suma(num1,num2))