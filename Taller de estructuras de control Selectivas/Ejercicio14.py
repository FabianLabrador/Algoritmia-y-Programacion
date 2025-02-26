lectura_anterior = int(input("Ingrese la lectura anterior: "))
lectura_actual = int(input("Ingrese la lectura actual: "))
consumo = lectura_actual - lectura_anterior

if consumo <= 100:
    costo = 4600
elif consumo <= 300:
    costo = 80000
elif consumo <= 500:
    costo = 100000
else:
    costo = 120000

monto = consumo * costo
print("Monto total a pagar:", monto)