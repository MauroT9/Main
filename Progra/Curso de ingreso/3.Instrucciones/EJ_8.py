#Ingresar 5 números enteros. Determinar el máximo y el mínimo.

i = 0
maximo = 0
minimo = 0

while i < 5:
    numero = int(input("Ingrese un número entero: "))
    
    if numero > maximo or i == 0:
        maximo = numero
    if numero < minimo or i == 0:
        minimo = numero

    i += 1

print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")