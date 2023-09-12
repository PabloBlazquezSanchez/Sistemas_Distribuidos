"""
Este programa ha sido realizado por Pablo Blázquez Sánchez.
Este programa sirve para encriptar y desencriptar mensajes. Presenta muchas funciones el encriptar y desencriptar mensajes:
    comunicarte con amigos de una manera divertida, hablar de temas privados, etc.
"""
alfb = "abcdefghijklmnñopqrstuvwxyz" #Aquí creamos el abecedario del que sacaremos el valor del carácter
crmess = "" #Variables de texto
uncrmess = ""

print("Hola! Este programa sirve para encriptar mensajes y desencriptar mensajes encriptados, mediante \"cifrado César\".")
print("En este programa, la clave de cifrado y descifrado es la que acordaréis entre vosotros.")
print("Si deseas encriptar un mensaje, escribe \"cr\", y si deseas desencriptar un mensaje, escribe \"uncr\".")
resp = input()

if resp == "cr":
    message = input("Introduzca a continuación el mensaje a encriptar: ") #Mensaje que se introduce para encriptar
    clav = int(input("Introduzca a continuación la clave que desea utilizar para encriptar: ")) #Declarar variable clave
    #Lo que viene ahora es el proceso de encriptado, esto es, junto con la variable "clav" las letras de la palabra van a cambiar
    #para encriptarlo y hacerlo difícil de entender.
    message = message.replace("á", "a").replace("é", "e").replace("í","i").replace("ó","o").replace("ú","u") #Convierte las vocales con tilde en vocales sin tilde
    for caracter in message:
        if caracter in alfb:
            position = alfb.find(caracter) #se crea una variable posición que va a guardar el dato numérico del caracter
            newpos = (position + clav) % 27 #El valor númerico máximo de la nueva posición va a ser 27, ya que no hay más letras en el abecedario
            newchar = alfb[newpos]
            #print("El nuevo caracter es: ", newchar)
            crmess += newchar
        else:
            crmess += caracter #Esto incluye los caracteres que no estén en la variable alfb
    print ("Tu mensaje encriptado es:", crmess)

#Para desencriptar, el proceso viene a ser el mismo pero al dar el valor a newpos se resta la clave en vez de sumarla
if resp == "uncr":
    crypmess = input("Introduzca el mensaje encriptado a desencriptar: ")
    clav = int(input("Introduzca a continuación la clave que desea utilizar para desencriptar: "))
    for caracter in crypmess:
        if caracter in alfb:
            position = alfb.find(caracter)
            newpos = (position - clav) % 27
            newchar = alfb[newpos]
            uncrmess += newchar
        else:
            uncrmess += caracter
    print("Tu mensaje desencriptado es: ", uncrmess)