# Programa realizado por Pablo Blázquez Sánchez
# Este programa consiste en que introduces el año en el que naciste
# y luego introduces el año en el que estás. Automáticamente te dirá
# la edad que tienes y la edad que tendrías si fueras un perro.
print("Prpiedad de Pablo Blázquez Sánchez, 2ºBTO D.")
print("Hola! Bienvenido a mi programa de calculador de edades!")
print("Antes de realizarte las preguntar para adivinar tu edad, ")
print("me gustaría que vieras esta obra de arte creada con ASCII.")
print("Es un perro.")
print("          __")
print(" \ ______/ V`-,")
print("  }        /~~")
print(" /_)^ --,r'      ___")
print("|b      |b      /___\ ")
nacimiento = int(input("Introduce el año en el que naciste: ")) #Esto declara una variable numérica llamada nacimiento, donde debes introducir el año de nacimiento
año_realizacion = int(input("Introduce el año en el que estás: ")) #Esto declara una variable también numérica llamada Año de realización, igual a la anterior
print("Ten en cuenta que lo hacemos con el año, despreciamos")
print("el mes y día de nacimiento.")
edad = año_realizacion - nacimiento #Variable edad (la humana)
print("Tu edad es", edad, "años.") #Esto muestra tu edad humana en pantalla
edad_perro = edad*7 #Variable edad (la de perro)
print("Ahora, si fueras un perro tendrías", edad_perro, "años.") #Esto muestra en pantalla tu edad de perro