ventas = input("Ingrese las ventas del departamento separadas con comas: ")
(Departamento1,Departamento2,Departamento3)=ventas.split(",")

Departamento1=int(Departamento1)
Departamento2=int(Departamento2)
Departamento3=int(Departamento3)

total_ventas = Departamento1+Departamento2+Departamento3
salario = int(input("Ingrese el salario mensual del vendedor: "))

if(Departamento1>total_ventas/3):
    print("Salario vendedor departamento1:",salario*0.20+salario, "Departamentos 2 y 3 tendran un salario de: ",salario)

elif(Departamento2>total_ventas/3):
    print("Salario vendedor departamento2:",salario*0.20+salario, "Departamentos 1 y 3 tendran un salario de: ",salario)

elif(Departamento3>total_ventas/3):
    print("Salario vendedor departamento3:",salario*0.20+salario, "Departamentos 1 y 2 tendran un salario de: ",salario)

