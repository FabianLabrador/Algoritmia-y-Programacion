
import math
#Entradas
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))
#Salidas
s = (lado1 + lado2 + lado3) / 2
area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

print("El área del triángulo es:",area)