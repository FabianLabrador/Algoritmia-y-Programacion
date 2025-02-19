#Entradas
sueldo_base = float(input("Ingrese el sueldo base del vendedor:"))
venta1 = float(input("Ingrese el valor de la venta #1: "))
venta2 = float(input("Ingrese el valor de la venta #2: "))
venta3 = float(input("Ingrese el valor de la venta #3: "))
 #Salidas  
comisiones = (venta1 + venta2 + venta3) * 0.10
sueldo_total = sueldo_base + comisiones
print("Las comisiones suman un valor de : $",comisiones," y un Total",sueldo_total)