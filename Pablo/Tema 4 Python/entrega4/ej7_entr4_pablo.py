"""
Entrega 4: ejercicio 7
Programa realizado por Pablo Blázquez Sánchez
Este programa, desde un diccionario, va a imprimir los elementos individualmente,
luego va a imprimir las claves y por último va a imprimir los valores.
"""
dictA7 = {
    "Empresa desarrolladora":"Polyphony Digital",
    "Distribuidor":"Sony",
    "Serie de videojuegos":"Gran Turismo",
    "Entrega":"Gran Turismo 5",
    "Año de lanzamiento":"2010",
    "Catalogado":3
    }
print("""Este programa, desde un diccionario, va a imprimir primero las claves,
luego va a imprimir los valores y por último va a imprimir todo por separado.""")
print("Primero le mostraremos el diccinario:")
print(dictA7)
print("Ahora le mostraremos sólo las claves:")
for x in dictA7:
    print(x)
print("Ahora sólo los valores:")
for x in dictA7:
    print(dictA7[x])
print("Ahora todo por separado:")
for x,y in dictA7.items():
    print(x,y)