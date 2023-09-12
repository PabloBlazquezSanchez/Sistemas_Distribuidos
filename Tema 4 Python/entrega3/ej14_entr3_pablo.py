listaA10 = []
print("Este programa te pide 5 elementos cualesquiera, los introduce en una lista, muestra la lista y luego los ordena de manera ascendente y descendente")
for x in range(5):
    x = input("Introduzca a continuación un elemento: ")
    listaA10.append(x)
print("La lista sin modificar con los elemento introducidos es:", listaA10)
listaA10.sort()
print("La lista ordenada de manera ascendente es:", listaA10)
listaA10.sort(reverse = True)
print("La lista ordenada de manera descendente es:", listaA10)