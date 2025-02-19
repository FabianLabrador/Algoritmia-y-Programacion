#Entrads
x = int(input("Ingrese la cantidad de naranjas compradas: "))
y = float(input("Ingrese el precio por docena: "))
k = float(input("Ingrese el monto total de la venta: "))

costo_total = (x / 12) * y
porcentaje_ganancia = ((k - costo_total) / costo_total) * 100
print("El porcentaje de ganancia obtenida en la inversión es: ",porcentaje_ganancia)