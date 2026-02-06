n = input("Entrada: ")

try:
    n = int(n)
    print("Es un entero")
except ValueError:
    print("No es un entero")
finally:
    print("Fin de la ejecución")