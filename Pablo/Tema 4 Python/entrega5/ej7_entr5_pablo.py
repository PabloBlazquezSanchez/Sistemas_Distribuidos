"""
Entrega 5: ejercicio 7
Programa realizado por Pablo Blázquez Sánchez
"""
def subrayado (a,b = "*"):
    print(a)
    print(b*len(a))
texto = input("Introduzca a continuación un texto cualquiera: ")
print("Ahora se va a mostrar el texto subrayado con asteriscos")
subrayado(texto)
print("Ahora se va a mostrar el texto subrayado con guiones")
subrayado(texto,"-")