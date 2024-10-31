#A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. 
#Para serlo el mismo deberá medir más de 1.80 metros.

altura = float(input("Ingrese una altura"))

if altura >= 1.80:
    print("Usted es pivot")
else:
    print("Usted no es pivot")
