"""
Entrega 5: ejercicio 4
Programa realizado por Pablo Blázquez Sánchez
Este programa te pide números hasta que el número introducido sea 0. Luego
muestra en pantalla la suma de los números introducidos y el número de intentos necesitados
"""
def ej_4():
    intentos = 0
    suma = 0
    while True:
        num = eval(input("Introduzca a continuación un número: "))
        if num != 0:
            suma+=num
            intentos+=1
            print("Intento", intentos)
            print("El valor de la suma es", suma)
            print("Inténtelo de nuevo")
        else:
            print("Has introducido el 0 en el intento", intentos+1, ", enhorabuena!")
            print("La suma de todos los números que has introducido es", suma)
            break
ej_4()