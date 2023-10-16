listaA8 = ["piña","platano","albaricoque","kiwi","cereza","nectarina","higo"]
newList = []
print("Este prtograma, mediante un bucle for, va a crear una lista sólo con las palabras que contengan la letra \"e\".")
print("La lista principal es:", listaA8)
for x in listaA8:
    if "e" in x:
        newList.append(x)
print("La lista con los elementos que contienen la letra \"e\" son:", newList)