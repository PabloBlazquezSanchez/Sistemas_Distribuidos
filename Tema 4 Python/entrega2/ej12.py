print("Este programa consiste en que introduces un texto cualquiera y te saca partes de ese texto, ya sean letras ó sílabas")
texto = input("Introduce un texto cualquiera a continuación, por ejemplo tu primer apellido: ")

print("Si tomamos nuestro punto de referencia en el principio, encontramos lo siguiente:")
print("Un carácter concreto, en este caso el tercer carácter del apellido (tenemos en cuenta el carácter 0):", texto[3])
print("Un tramo intermedio cualquiera, que no contenga ni la primera ni la segunda letra:", texto[2:5])
print("Un tramo escogido desde el principio:", texto[:5])
print("Un tramo escogido desde un carácter x hasta el final del texto:", texto[3:])

print("Ahora, si tomamos nuestro punto de referencia en el final del texto, encontramos lo siguiente:")
print("""¡¡DATO!! Cuando cogemos el punto de referencia en el final del texto, los carácteres van a ser negativos,
        esto es, va a ser, por ejemplo, -3 en vez de 3 porque debe retroceder hasta el principio de la palabra.""")
print("Un carácter concreto, por ejemplo la segunda letra empezando por el final ([-2]):", texto[-2])
print("Un tramo intermedio, con la misma condición que antes (de [-5] a [-3]:", texto[-5:-3])
print("Un tramo desde cualquier carácter hasta el final (desde [-5])", texto[-5:])