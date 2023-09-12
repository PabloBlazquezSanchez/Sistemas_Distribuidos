"""
Entrega 4: ejercicio 6
Programa realizado por Pablo Blázquez Sánchez
Este programa muestra un diccionario inicial, luego cambia el valor de un elemento,
añade un nuevo elemento y lo vuelve a mostrar en pantalla. Después, coge dos elementos de
esa lista y los elimina.
"""
dictA6 = {
    "Asignatura":"Tecnología Industrial",
    "Alumno":"Pablo Blázquez Sánchez",
    "Nota de examen":7.7,
    }
print("Ahora se va a mostrr un diccionario inicial:")
print(dictA6)
print("A continuación, se va a mostrar el mismo diccionario pero con la \"Nota de examen\" cambiada y con el elemento \"Media evaluación\" añadido.")
dictA6["Nota de examen"] = 10
dictA6["Media evaluación"] = 9.9
print(dictA6)
print("Ahora, vamos a volver a mostrar el diccionario pero con los elementos \"Nota de examen\" y \"Media de evaluación\" borrados:")
dictA6.pop("Nota de examen")
dictA6.pop("Media evaluación")
print(dictA6)