"""
Entrega 4: ejercicio 5
Programa realizado por Pablo Blázquez Sánchez
Este programa muestra un diccionario inicial, luego cambia el valor de un elemento,
añade un nuevo elemento y lo vuelve a mostrar en pantalla.
"""
dictA5 = {
    "Asignatura":"Tecnología Industrial",
    "Alumno":"Pablo Blázquez Sánchez",
    "Nota de examen":7.7,
    }
print("Ahora se va a mostrr un diccionario inicial:")
print(dictA5)
print("A continuación, se va a mostrar el mismo diccionario pero con la \"Nota de examen\" cambiada y con el elemento \"Media evaluación\" añadido.")
dictA5["Nota de examen"] = 10
dictA5["Media evaluación"] = 9.9
print(dictA5)