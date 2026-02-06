# Lista para guardar las tuplas de números complejos
complejos = []

print("Introduce números complejos (ej: 3+4j).")

while True:
    entrada = input("Ingresa un número complejo: ")
    if entrada == "":
        break
    try:
        num = complex(entrada)  # Convertir a número complejo
        tupla = (num, -num, num.conjugate())  # (original, opuesto, conjugado)
        complejos.append(tupla)
    except ValueError:
        print("Entrada inválida. Usa el formato a+bj, por ejemplo 3+4j.")

# Mostrar resultados
print("\nNúmeros complejos y sus propiedades:")
for t in complejos:
    original, opuesto, conjugado = t
    print(f"Número: {original}, Opuesto: {opuesto}, Conjugado: {conjugado}")
