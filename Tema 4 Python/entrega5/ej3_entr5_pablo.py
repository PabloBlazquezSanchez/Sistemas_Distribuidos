"""
Entrega 5: ejercicio 3
Programa realizado por Pablo Blázquez Sánchez
Este programa verifica si tu dirección de correo electrónico es válida o no
(debe contener el @).
"""
def verificar(s):
    if "@" in s:
        print("Su dirección de correo electrónico es válida.")
    else:
        print("Su dirección de correo electrónico no es válida.")
print("Veamos si su dirección de correo electrónico es válida o no.")
correo = input("Introduzca su dirección de correo electrónico: ")
verificar(correo)