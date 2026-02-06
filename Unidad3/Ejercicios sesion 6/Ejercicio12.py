# Lista para guardar los puntos
puntos = []

# Número de puntos
n = int(input("¿Cuántos puntos quieres introducir? "))

for i in range(n):
    print(f"\nPunto {i+1}:")
    x = float(input("Ingresa coordenada x: "))
    y = float(input("Ingresa coordenada y: "))
    z = float(input("Ingresa coordenada z: "))
    
    # Determinar octante
    if x > 0 and y > 0 and z > 0:
        octante = 1
    elif x < 0 and y > 0 and z > 0:
        octante = 2
    elif x < 0 and y < 0 and z > 0:
        octante = 3
    elif x > 0 and y < 0 and z > 0:
        octante = 4
    elif x > 0 and y > 0 and z < 0:
        octante = 5
    elif x < 0 and y > 0 and z < 0:
        octante = 6
    elif x < 0 and y < 0 and z < 0:
        octante = 7
    elif x > 0 and y < 0 and z < 0:
        octante = 8
    else:
        octante = 0  # Punto sobre algún plano
    
    # Guardar el punto como tupla de 4 elementos
    punto = (x, y, z, octante)
    puntos.append(punto)

# Mostrar todos los puntos
print("\nPuntos ingresados:")
for p in puntos:
    x, y, z, octante = p
    if octante == 0:
        print(f"El punto ({x}, {y}, {z}) está sobre algún plano y no pertenece a ningún octante.")
    else:
        print(f"El punto ({x}, {y}, {z}) pertenece al octante {octante}")
