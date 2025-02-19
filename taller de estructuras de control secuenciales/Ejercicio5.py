# Entradas

parcial1 = float(input("Ingrese la primera calificación : "))
parcial2 = float(input("Ingrese la segunda calificación : "))
parcial3 = float(input("Ingrese la tercera calificación : "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

#Salidas

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print("La calificación final es: ",calificacion)