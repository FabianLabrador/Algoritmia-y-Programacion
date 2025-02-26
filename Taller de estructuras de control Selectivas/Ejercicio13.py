dia, mes, año = input("Ingrese su fecha de nacimiento (DD/MM/YYYY): ").split("/")
dia = int(dia)
mes = int(mes)
año = int(año)
edad = 2024 - año

if (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
    signo = "Acuario"
elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 19):
    signo = "Piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = "Aries"
elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
    signo = "Tauro"
elif (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
    signo = "Géminis"
elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    signo = "Leo"
elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpión"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
else:
    signo = "Capricornio"

print("Signo zodiacal:", signo, "Edad:", edad)