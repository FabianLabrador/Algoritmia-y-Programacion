#Entradas 
sueldo_base = float(input("Ingrese el sueldo base: "))
horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
#Operaciones
pago_hora_extra = (sueldo_base / 160) * 1.25 * horas_extras
deducciones = sueldo_base * (0.05 + 0.02 + 0.07)
#Entrda2
asignaciones = 250000 + (173000 * int(input("Ingrese el número de hijos: "))) + 180000
#Salidas
salario_neto = sueldo_base + pago_hora_extra + asignaciones - deducciones
print(f"El salario neto es: $",salario_neto)
