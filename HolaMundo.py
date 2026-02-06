salario = float(input("Ingrese el salario del trabajador: "))
 
if salario >= 5000:
    porcentaje_bono = 0.05
else:
    porcentaje_bono = 0.15  
 
bono = salario * porcentaje_bono
 
print(f"El bono correspondiente es: ${bono:.2f}")
print(f"El total a recibir (Salario + Bono) es: ${salario + bono:.2f}")
 
print("Proceso de cálculo finalizado con exito ")
 