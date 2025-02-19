#entradas
galones = float(input("Ingrese la cantidad de galones surtidos: "))
#salidas
precio_litro = 50000
litros = galones * 3.785
total_pagar = litros * precio_litro
print("El valor total por la gasolina es:",total_pagar)