# Crear lista 1
arr1 = []
print("Creando la primera lista. Deja el elemento vacío para terminar.")
while True:
    elem = input("Ingresa un elemento para arr1: ").strip()
    if elem == "":
        break
    if elem not in arr1:  # Solo elementos únicos
        arr1.append(elem)

# Crear lista 2
arr2 = []
print("\nCreando la segunda lista. Deja el elemento vacío para terminar.")
while True:
    elem = input("Ingresa un elemento para arr2: ").strip()
    if elem == "":
        break
    if elem not in arr2:
        arr2.append(elem)

# Convertimos a conjuntos para facilitar cálculos
set1 = set(arr1)
set2 = set(arr2)

# Elementos en ambas listas
interseccion = set1 & set2

# Elementos que aparecen en una sola lista
solo_una_lista = (set1 ^ set2)

# Elementos restantes en arr1 tras extraer arr2
restantes_arr1 = set1 - set2

# Elementos restantes en arr2 tras extraer arr1
restantes_arr2 = set2 - set1

# Mostrar resultados
print("\nResultados:")
print(f"Elementos en ambas listas ({len(interseccion)}): {list(interseccion)}")
print(f"Elementos que aparecen en solo una lista ({len(solo_una_lista)}): {list(solo_una_lista)}")
print(f"Elementos restantes en arr1 tras extraer arr2 ({len(restantes_arr1)}): {list(restantes_arr1)}")
print(f"Elementos restantes en arr2 tras extraer arr1 ({len(restantes_arr2)}): {list(restantes_arr2)}")
