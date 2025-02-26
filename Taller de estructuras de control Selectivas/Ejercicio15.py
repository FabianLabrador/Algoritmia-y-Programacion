edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (M/F): ")
hemoglobina = float(input("Ingrese nivel de hemoglobina: "))

if edad <= (1/12) and 13 <= hemoglobina <= 26:
    resultado = "No tiene anemia"
elif 1/12 < edad <= 0.5 and 10 <= hemoglobina <= 18:
    resultado = "No tiene anemia"
elif 0.5 < edad <= 1 and 11 <= hemoglobina <= 15:
    resultado = "No tiene anemia"
elif 1 < edad <= 5 and 11.5 <= hemoglobina <= 15:
    resultado = "No tiene anemia"
elif 5 < edad <= 10 and 12.6 <= hemoglobina <= 15.5:
    resultado = "No tiene anemia"
elif 10 < edad <= 15 and 13 <= hemoglobina <= 15.5:
    resultado = "No tiene anemia"
elif sexo == "F" and edad > 15 and 12 <= hemoglobina <= 16:
    resultado = "No tiene anemia"
elif sexo == "M" and edad > 15 and 14 <= hemoglobina <= 18:
    resultado = "No tiene anemia"
else:
    resultado = "Tiene anemia"

print(resultado)