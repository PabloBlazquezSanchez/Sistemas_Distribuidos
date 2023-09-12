listaA5 = ["higo","pipas","patata","cacahuetes","almendras"]
print("Este programa va a ir mostrando la misma lista pero eliminando un elemento dos veces y luego se elimina la lista.")
print("La lista original, es decir, sin modificar nada es:", listaA5)
listaA5.remove("patata")
print("Si eliminamos la palabra \"patata\", la lista queda así:", listaA5)
listaA5.pop(1)
print("Si después eliminamos el segundo elemento, la lista quedará así:", listaA5)
listaA5.clear()
print("Por último, si eliminamos todos los elementos, la lista quedará así:", listaA5)