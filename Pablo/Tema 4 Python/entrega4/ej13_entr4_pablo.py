"""
Entrega 4: ejercicio 13
Programa realizado por Pablo Blázquez Sánchez
Este programa imprime los 10 primeros números excepto el 5.
"""
num = 0
print("A continuación, le vamos a mostrar los 10 primeros números excepto el 5:")
while num<10:
    num+=1
    if num == 5:
        continue
    print(num)