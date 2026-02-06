complejos = []

print("Introduce números complejos (ej: 3+4j).")

while True:
    entrada = input("Ingresa un número complejo: ")
    if entrada == "":
        break
    try:
        num = complex(entrada) 
        tupla = (num, -num, num.conjugate()) 
        complejos.append(tupla)
    except ValueError:
        print("Entrada inválida. Usa el formato a+bj, por ejemplo 3+4j.")

print("\nNúmeros complejos y sus propiedades:")
for t in complejos:
    original, opuesto, conjugado = t
    print(f"Número: {original}, Opuesto: {opuesto}, Conjugado: {conjugado}")
