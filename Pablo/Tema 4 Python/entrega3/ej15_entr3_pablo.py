listaA11 = []
print("Este programa te pide 5 elementos cualesquiera, los introduce en una lista, muestra la lista y luego los ordena de manera ascendente y descendente")
print("sin tener en cuenta las mayúsculas o minúsculas")
elem1 = input("Introduce el primer elemento: ")
elem2 = input("Introduce el segundo elemento: ")
elem3 = input("Introduce el tercer elemento: ")
elem4 = input("Introduce el cuarto elemento: ")
elem5 = input("Introduce el quinto elemento: ")
for x in elem1, elem2, elem3, elem4, elem5:
    listaA11.append(x)
print("La lista sin modificar con los elemento introducidos es:", listaA11)
listaA11.sort(key = str.lower)
print("La lista ordenada de manera ascendente es:", listaA11)
listaA11.sort(reverse = True, key = str.lower)
print("La lista ordenada de manera descendente es:", listaA11)