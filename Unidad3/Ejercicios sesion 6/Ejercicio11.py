palabras = []

print("Introduce palabras.")
while True:
    palabra = input("Ingresa una palabra: ").strip()
    if palabra == "":
        break
    palabras.append(palabra)

tupla_palabras = tuple(palabras)

if len(tupla_palabras) >= 1:
    primera, *_, ultima = tupla_palabras
    print(f"\nPrimera palabra: {primera}")
    print(f"Última palabra: {ultima}")
else:
    print("\nNo se ingresaron palabras.")
