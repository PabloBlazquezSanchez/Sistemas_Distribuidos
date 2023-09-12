"""
Entrega 5: ejercicio 2
Programa realizado por Pablo Blázquez Sánchez
Este programa te muestra la tabla de multiplicar de un número introducido por el usuario
"""
rel=[]
k = 0
num1 = eval(input("Introduzca el número del que deseas hacer la tabla de multiplicar: "))
def tabla(a):
    for k in range(11):
        val = a*k
        rel.append(val)
        k+=1
    return rel
print("La tabla de multiplicar de", num1, "es:")
for x in tabla(num1): print(x)