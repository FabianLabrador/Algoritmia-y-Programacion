#Entradas
lectura_anterior = float(input("Ingrese la lectura pasada en kWh: "))
lectura_actual = float(input("Ingrese la lectura actual en kWh: "))
costo_kwh = float(input("Ingrese el costo por kWh: "))
#Salida
consumo = lectura_actual - lectura_anterior
total_pagar = consumo * costo_kwh
print(f"El valor total a pagar por el consumo es: $",total_pagar)