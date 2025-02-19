# Entradas
precio_contado = float(input("Ingrese el precio del computador al contado (COP): "))
cuota_mensual = float(input("Ingrese el valor de cada cuota mensual (COP): "))

# Cálculo del precio total a cuotas y el recargo
precio_total_cuotas = cuota_mensual * 12
recargo = precio_total_cuotas - precio_contado
porcentaje_recargo = (recargo / precio_contado) * 100

# Salidas
print("El precio total pagando a cuotas es: ",precio_total_cuotas," COP")
print("El recargo total es: ",recargo," COP")
print("El porcentaje de recargo sobre el precio al contado es: ",porcentaje_recargo,"%")
