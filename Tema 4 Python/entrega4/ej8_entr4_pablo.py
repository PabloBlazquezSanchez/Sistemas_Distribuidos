"""
Entrega 4: ejercicio 8
Programa realizado por Pablo Blázquez Sánchez
Este programa, lo que va a hacer es meter 3 diccionarios en uno solo.
"""
dictA8_1 = {
    "Expediente nº":14576,
    "Delito":"Asesinato múltiple",
    "Nombre y apellido del acusado":"Boris Jhonson"
    }
dictA8_2 = {
    "Declaración del Jurado":"El acusado es culpable de todos los asesinatos",
    "Nº de testigos":5,
    "Nº de personas llamadas a declarar":2
    }
dictA8_3 = {
    "Sentencia":"Cadena perpetua",
    "Declaraciones del acusado":"Ninguna",
    "Prisión de envío":"Prisión de Belmarsh"
    }
print("A continuación, vamos a unir tres diccionarios creados anteriormente:")
dictA8 = {
    "Datos básicos":dictA8_1,
    "Declaraciones":dictA8_2,
    "Fin del juicio":dictA8_3
    }
print(dictA8)