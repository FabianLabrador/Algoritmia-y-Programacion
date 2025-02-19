#Entradas
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio por hora: "))
#Salidas
sueldo_bruto = horas_trabajadas * precio_hora
impuestos = sueldo_bruto * 0.20
sueldo_neto = sueldo_bruto - impuestos
print("El salario neto menos los impuestos es: $", sueldo_neto)