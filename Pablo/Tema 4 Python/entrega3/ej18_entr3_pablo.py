listaA13 = ["Perro","Gato","Mono","Elefante"]
print("Este programa coge una lista, ya definida por el programador, guarda una copia en una segunda variable, invierte el orden de esa varible")
print("y muestra en pantalla la variable original y la copia invertida. Luego, muestra en pantalla una tercera variable")
print("que es la unión de las dos variables anteriores")
listaA14 = listaA13.copy()
listaA14.reverse()
print("La lista original es:", listaA13)
print("La copia invertida de la lista anterior es:", listaA14)
listaA15 = listaA13 + listaA14
print("La unión de estas dos variables queda así:", listaA15)