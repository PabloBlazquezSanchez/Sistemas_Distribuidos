"""
Entrega 4: ejercicio 14
Programa realizado por Pablo Blázquez Sánchez
Este programa va a preguntar un número entre 1 y 5 hasta que diga el número correcto.
"""
num = 0
intentos = 0
print("Intenta adivinar qué número del 1 al 5 tengo en la mente")
while num != 3:
    intentos+=1
    num = eval(input())
    if num == 3:
        print("¡Correcto, has acertado! Has acertado en el intento", intentos)
        break
    print("Inténtelo de nuevo")