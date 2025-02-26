monto = int(input("Ingrese el monto de la compra: "))
if monto < 50000:
    descuento = 0
elif monto <= 100000:
    descuento = 0.05
elif monto <= 700000:
    descuento = 0.11
elif monto <= 1500000:
    descuento = 0.18
else:
    descuento = 0.25

pago = monto - (monto * descuento)
print("Monto a pagar:", pago, "Descuento aplicado:", descuento * 100, "%")