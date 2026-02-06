n = int(input("Ingrese el tamaño de la matriz identidad (n x n): "))

identidad = []

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)  
        else:
            fila.append(0)  
    identidad.append(fila)

print("\nMatriz identidad:")
for fila in identidad:
    print(fila)
    

