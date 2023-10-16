"""
Entrega 4: ejercicio 11
Programa realizado por Pablo Blázquez Sánchez
Este programa determina si un alumno aprueba o no una asignatura dependiendo de
las notas que saque en los exámenes y en las prácticas.
"""
print("""Veamos si puedes aprobar la asignatura. Para aprobar esta asignatura
    debes tener un 5 o mas en la media de exámenes ó tener un 7 o más en la media de las prácticas.""")
m_ex = eval(input("Introduzca a continuación la nota media de los exámenes (puedes introducirlo con decimales): "))
m_pr = eval(input("Introduzca a continuación la nota media de las práctcas (puedes introducirlo con decimales): "))
if m_ex >= 5 or m_pr >= 7:
    print("!Felicidades! Has superado la asignatura.")
else:
    print("Lo sentimos pero no has superado la asignatura.")