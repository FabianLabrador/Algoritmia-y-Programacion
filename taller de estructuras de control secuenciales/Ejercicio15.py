#Entradas
precio_final = float(input("Ingrese el precio final pagado: "))
pvp = float(input("Ingrese el precio de venta al público: "))
#Salidas
descuento = ((pvp - precio_final) / pvp) * 100

print("El porcentaje de descuento  es: ",descuento)