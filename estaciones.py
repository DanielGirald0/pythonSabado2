# calcular estacion del año segun la fechas
print("Digite la fecha para calcular estacion climatica")
mes = int(input("Digite mes: "))
dia = int(input("Digite dia: "))

if mes == 1 or mes == 2 or mes == 12:
    estacion = "invierno"
elif mes == 3:
    if dia < 20:
        estacion = "invierno"
    else:
        estacion = "primavera"
elif mes == 4 or mes == 5:
    estacion = "primavera"
elif mes == 6:
    if dia < 21:
        estacion = "primavera"
    else:
        estacion = "verano"
elif mes == 7 or mes == 8:
    estacion = "verano"
elif mes == 9:
    if dia < 22:
        estacion = "verano"
    else:
        estacion = "otoño"
elif mes == 10 or mes == 11:
    estacion = "otoño"
else:
    estacion = None

if estacion:
    print(f"La estación del año para el dia {dia} del mes {mes} es: {estacion}.")
else:
    print("La fecha ingresada no es valida.")
