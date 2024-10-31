#Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de
#aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el
#usuario.

sueldo = float(input("Ingrese su sueldo: "))
porcentaje_aumento = float(input("Ingrese el porcentaje de aumento: "))

aumento = sueldo * porcentaje_aumento / 100
sueldo_aumentado = sueldo + aumento

print(f"Su sueldo aumentado es {sueldo_aumentado}")
