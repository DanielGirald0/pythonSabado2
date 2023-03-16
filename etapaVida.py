#Calcular la etapa de la vida segun la edad 
edad= int(input("Digite la edad: "))

if edad <= 14:
    print("Niño")
elif edad > 14 and edad <=28:
    print("Joven")
elif edad > 28 and edad <=60:
    print("Adulto")
elif edad > 60:
    print("Adulto mayor")
else:
    print("Edad invalida")



