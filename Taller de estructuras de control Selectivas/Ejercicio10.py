categoria = int(input("Ingrese la categoría del trabajador: "))
sueldo = int(input("Ingrese el sueldo bruto: "))
if categoria == 1:
    aumento = 0.10
elif categoria == 2:
    aumento = 0.15
elif categoria == 3:
    aumento = 0.20
elif categoria == 4:
    aumento = 0.40
elif categoria == 5:
    aumento = 0.60

nuevo_sueldo = sueldo + (sueldo * aumento)
print("Categoría:", categoria, "Nuevo sueldo:", nuevo_sueldo)