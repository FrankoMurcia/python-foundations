dic1 = {}
print("Creando Diccionario 1. Escribe.")
while True:
    clave = input("Ingresa la clave: ")
    if clave == "":
        break
    valor = input("Ingresa el valor: ")

    if valor.isdigit():
        valor = int(valor)
    if clave in dic1:
        if isinstance(dic1[clave], list):
            dic1[clave].append(valor)
        else:
            dic1[clave] = [dic1[clave], valor]
    else:
        dic1[clave] = [valor]  

dic2 = {}
print("\nCreando Diccionario 2. Escribe.")
while True:
    clave = input("Ingresa la clave: ")
    if clave == "":
        break
    valor = input("Ingresa el valor: ")
    if valor.isdigit():
        valor = int(valor)
    if clave in dic2:
        if isinstance(dic2[clave], list):
            dic2[clave].append(valor)
        else:
            dic2[clave] = [dic2[clave], valor]
    else:
        dic2[clave] = [valor]  

dic_combinado = {}

for clave, valor in dic1.items():
    dic_combinado[clave] = valor

for clave, valor in dic2.items():
    if clave in dic_combinado:
        dic_combinado[clave].extend(valor)
    else:
        dic_combinado[clave] = valor

print("\nDiccionario combinado:")
print(dic_combinado)
