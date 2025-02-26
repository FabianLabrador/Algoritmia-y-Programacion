#Entradas
Salario=int(input("Ingrese su salario: "))

if (Salario<900000):
    print("Su nuevo Salario es: $",((Salario*0.15)+Salario))

elif(Salario>=900000):
    print("Su nuevo Salario es: $",((Salario*0.12)+Salario))

