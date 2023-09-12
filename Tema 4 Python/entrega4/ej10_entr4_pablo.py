"""
Entrega 4: ejercicio 10
Programa realizado por Pablo Blázquez Sánchez
Este programa acepta o deniega la entrada a una fiesta en la que debes ser
mayor de 18 y de Talavera de la Reina.
"""
print("Para entrar a la fiesta, te haremos unas preguntas para ver si eres apto o no.")
age = int(input("Díganos su edad: "))
localidad = str(input("Díganos de dónde eres: "))
if age >= 18 and localidad == "Talavera de la Reina":
    print("Puedes pasar. Disfruta de la fiesta")
else:
    print("No puedes pasar debido a que no cumples una de las dos condiciones.")