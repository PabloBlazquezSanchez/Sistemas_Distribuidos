print("Este programa imprime diferentes partes de un texto")
name = input("Escribe tu nombre: ")

#Referenciado al principio del texto
print("-Primero veremos partes del texto referenciado al principio del texto:")
print("Carácter concreto, en este caso el [0]: " + name[0])
print("Tramo intermedio entre el [1] al [3]:" + name[1:3])
print("Tramo desde el principio hasta el [3]:" + name[:3])
print("Tramo hasta el final desde el [3]:" + name[3:])
#Referenciado al final del texto
print("-Ahora veremos partes del texto referenciado al final:")
print("Carácter concreto, en este caso el [-2]:" + name[-2])
print("Tramo intermedio entre el [-1] y [-3]:" + name[-3:-1])
print("Tramo hasta el final desde el [-3]:" + name[-3:])