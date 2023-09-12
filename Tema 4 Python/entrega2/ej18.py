"""
Este programa ha sido realizado por Pablo Blázquez Sánchez.
Este programa sirve para encriptar y desencriptar mensajes. Presenta muchas funciones el encriptar y desencriptar mensajes:
    comunicarte con amigos de una manera divertida, temas gubernamentales, códigos nucleares, etc.
"""
alfb = "abcdefghijklmnñopqrstuvwxyz" #Aquí creamos el abecedario del que sacaremos el valor del carácter
clav = int(3) #Incremento del valor del carácter
newmess = "" #Variables de texto

message = input("Introduzca a continuación el mensaje: ") #Mensaje que se introduce para encriptar
#Lo que viene ahora es el proceso de encriptado, esto es, junto con la variable "clav" las letras de la palabra van a cambiar
#para encriptarlo y hacerlo difícil de entender.
for caracter in message:
    if caracter in alfb:
        position = alfb.find(caracter) #se crea una variable posición que va a guardar el dato numérico del caracter
        newpos = (position + clav) % 27
        newchar = alfb[newpos]
        #print("El nuevo caracter es: ", newchar)
        newmess += newchar
    else:
        newmess += caracter
print ("Tu mensaje encriptado es:", newmess)