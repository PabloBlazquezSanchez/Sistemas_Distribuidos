from time import sleep
listaA7 = ["Pablo","Daniel","Antonio","Álvaro","Hugo","David","Jorge"]
print("Este programa te muestra en pantalla los elementos de una lista definida por el programador.")
print("Se mostrará un elemento por línea y se hará mediante un bucle \"for\".")
print("La lista creada por el programador es:", listaA7)
print("A continuación, se mostrará cada elemento de la lista individualmente, es decir, uno por cada línea.")
for x in range(len(listaA7)):
    print(listaA7[x])
    sleep(0.25)