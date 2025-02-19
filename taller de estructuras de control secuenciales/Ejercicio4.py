
#Entradas

precio_total = float(input("Ingrese el total de la compra: "))

#Salidas

descuento = precio_total * 0.15
precio_final = precio_total - descuento

print(f"El total con descuento es: $",precio_final)