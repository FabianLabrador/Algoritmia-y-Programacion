
#Entradas

bolivares_prestados = float(input("Ingrese la cantidad de bolívares prestados: "))
intereses_pagados = float(input("Ingrese la cantidad de intereses pagados: "))

tasa_anual = (intereses_pagados / (bolivares_prestados * 4)) * 100

print("El porcentaje anual cobrado por el préstamo es: ",tasa_anual)