P = int(input("Ingrese P: "))
Q = int(input("Ingrese Q: "))
expresion = P**3 + Q**4 - 2 * P**2
if expresion > 680:
    print(P, "y", Q, "satisfacen la expresión")
else:
    print(P, "y", Q, "no satisfacen la expresión")