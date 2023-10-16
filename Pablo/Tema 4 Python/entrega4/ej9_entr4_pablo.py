from time import sleep
"""
Entrega 4: ejercicio 9
Programa realizado por Pablo Blázquez Sánchez
Este programa dice si un dos números son iguales o uno es mayor que otro.
"""
print("Vamos a comparar a continuación dos números.")
a = int(input("Introduzca a continuación el primer número: "))
b = int(input("Introduzca a continuación el segundo número: "))
print("Veamos ahora si son iguales o si uno es mayor que otro")
sleep(0.5)
if a == b:
    print("Los dos números son iguales")
elif a > b:
    print("El primer número es mayor que el segundo")
else:
    print("El segundo número es mayor que el primero")