"""
Propietario: Pablo Blázquez Sánchez
Fecha: 5/02/2021
Este programa consiste en que, al introducir dos números, se va a realizar una
comparación y se imprimirá en pantalla cuál es el mayor y, además, se hará la
suma de los números introducidos
"""
print("Este programa averigua cuál es el mayor de dos números introducidos.")
num1 = input("Introduzca a continuación el primer número: ")
num2 = input("Introduzca a continuación el segundo número: ")
if num1>num2:
    print("El número mayor es el primero,", num1)
    
if num2>num1:
    print("El número mayor es el segundo,", num2)
print("Además la suma de estos dos números es:", num1+num2)