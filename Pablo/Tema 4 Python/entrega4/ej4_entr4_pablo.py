"""
Entrega 4: ejercicio 4
Programa realizado por Pablo Bázquez Sánchez
Este programa muestra si una clave se encuentra, o no, en un diccionario ya creado.
"""
dictA4 = {
    "Empresa desarrolladora":"Nintendo, Capcom",
    "Distribuidor":"Nintendo",
    "Saga de videojuegos":"The Legend of Zelda",
    "Entrega":"The Legend of Zelda: Majora's Mask",
    "Año de Lanzamiento":2000#,
    #"Catalogado":7
    }
print("A continuación, vamos a ver si la clave \"Catalogado\" se encuentra en el diccionario que ha sido creado con anerioridad:")
if "Catalogado" in dictA4:
    print("Sí, la clave \"Catalogado\" se encuentra dentro del diccionario.")
else:
    print("No, la clave \"Catalogado\" no se encuentra dentro del diccionario.")