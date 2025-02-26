temp = int(input("Ingrese la temperatura en Fahrenheit: "))
if temp > 85:
    print("Natación")
elif temp > 70:
    print("Tenis")
elif temp > 32:
    print("Golf")
elif temp > 10:
    print("Esquí")
else:
    print("Marcha")