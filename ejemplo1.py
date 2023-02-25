#Represa Hidroituanngo
#Entradas 
nivelAgua=float(input("Digite el nivel de agua: "))

#Proceso
if nivelAgua>=0 and nivelAgua<=250:
    print(f"El sensor marca {nivelAgua}, muy bajo")
elif nivelAgua>250 and nivelAgua<=400:
    print(f"El sensor marca {nivelAgua}, optimo")
else:
     print(f"El sensor marca {nivelAgua}, PELIGRO")