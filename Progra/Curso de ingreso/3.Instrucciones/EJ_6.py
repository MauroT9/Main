#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
#Calcular la suma de los números ingresados y el promedio de los mismos.

bandera = True
acumulador = 0
i = 0

while bandera == True:
    numero = int(input("Ingrese un numero: "))
    seguir = input("Desea continuar (si / no): ")
    acumulador += numero
    i += 1
    if seguir == "no":
        bandera = False

promedio = acumulador / i

print(f"La suma acumulada es: {acumulador}")
print(f"El promedio es: {promedio}")
