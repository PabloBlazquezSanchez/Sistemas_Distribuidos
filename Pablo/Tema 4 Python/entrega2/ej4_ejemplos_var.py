ejemploCamelCase = "misNotasInstituto"
EjemploPascalCase = "EdadPadresTalavera"
ejemplo_snake_case = "padres_organizacion"
print("Hola! Este programa muestra ejemplos de los tres estilos para poner")
print("nombres a las variables.")
print("Si quieres ver un ejemplo de Camel Case escribe CC")
print("Si quieres ver un ejemplo de Pascal Case escribe PC")
print("Si quieres ver un ejemplo de Snake Case escribe SC")
print("Importante! Debes introducirlo en mayúsculas.")
resp = input("Introduce tu respuesta: ")
if resp == "CC":
    print("Un ejemplo de Camel Case es:", ejemploCamelCase)
    print("En Camel Case, la primera letra de cada palabra de la variable")
    print("está en mayúscula excepto la primera.")
if resp == "PC":
    print("Un ejemplo de Pascal Case es:", EjemploPascalCase)
    print("En Pascal Case, la primera letra de cada palabra de la variable")
    print("está en mayúscula.")
if resp == "SC":
    print("Un ejemplo de Snake Case es:", ejemplo_snake_case)
    print("En Snake Case, la variable lleva una _ después de cada palabra en la variable.")