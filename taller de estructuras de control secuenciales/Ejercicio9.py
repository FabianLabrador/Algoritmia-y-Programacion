# Entradas
chelines = float(input("Ingrese la cantidad en chelines austríacos: "))
dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
pesetas = float(input("Ingrese la cantidad en pesetas: "))

# Conversión
pesetas_chelines = (chelines * 956.871) / 100
francos_dracmas = (dracmas * 88.607) / 100 / 20.110
dolares = pesetas / 122.499
liras = (pesetas / 9.289) * 100

# Salidas
print(chelines,"chelines austríacos equivalen a ",pesetas_chelines,"pesetas.")
print(dracmas," dracmas griegos equivalen a ",francos_dracmas," francos franceses.")
print(pesetas," pesetas equivalen a ",dolares,"dólares estadounidenses.")
print(pesetas," pesetas equivalen a ",liras" liras italianas.")
