lista1 = ["Lechuga","Tomate","Coliflor"]
lista2 = ["Berenjena","Zanahoria", "Puerros"]
print("Este programa sirve para unir dos listas mediante el bucle for.")
print("Las dos listas de partida son:", lista1, "y", lista2)
print("Ahora vamos a emplear el bucle for y el método append para unir la lista1 a lista2")
for x in lista1:
    lista2.append(x)
print("El resultado de la unión es:", lista2)