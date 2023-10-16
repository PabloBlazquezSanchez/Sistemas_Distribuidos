listaA12 = []
print("Este programa te pide 5 elementos cualesquiera, los introduce en una lista, muestra la lista y luego invierte la lista y también la muestra.")
for x in range(5):
    elem = input("Introduzca un elemento: ")
    listaA12.append(elem)
print("La lista sin modificar con los elemento introducidos es:", listaA12)
listaA12.reverse()
print("La lista inversa queda así:", listaA12)