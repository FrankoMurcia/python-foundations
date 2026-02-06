n = int(input("Ingrese el numero de filas: "))
m = int(input("Ingrese el numero de columnas: "))

matriz = []

for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Ingrese el valor para la posicion [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nMatriz: ")
for fila in matriz:
    print(fila)

for j in range(m):
    suma_columna = 0 
    for i in range(n):
        suma_columna = += matriz[i][j]

    if suma_columna > 50: 
        print(f"La columna {j} ha excedido la cantidad")
        