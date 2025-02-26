monto_compra = float(input("Ingrese el monto total de la compra: "))
if monto_compra > 5000000:
    inversion = monto_compra * 0.55
    prestamo_banco = monto_compra * 0.30
    credito_fabricante = monto_compra * 0.15
else:
    inversion = monto_compra * 0.70
    prestamo_banco = 0
    credito_fabricante = monto_compra * 0.30

intereses = credito_fabricante * 0.20

print(f"Inversión propia: ${inversion}")
print(f"Préstamo del banco: ${prestamo_banco}")
print(f"Crédito al fabricante: ${credito_fabricante}")
print(f"Intereses a pagar: ${intereses}")