#Ingresar números enteros hasta que el usuario desee. 
#Determinar el máximo y el mínimo.

maximo = 0
minimo = 0
seguir = "si"
bandera_primero = False

while seguir == "si":
    numero = int(input("Ingrese un número entero: "))
    
    if numero > maximo or bandera_primero == False:
        maximo = numero
    if numero < minimo or bandera_primero == False:
        minimo = numero

    bandera_primero = True

    seguir = input("Ingresa otro? si/no ")

print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")