#Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.

i = 0
acumulador = 0
while i < 5:
    numero = int(input("Ingrese un numero: "))
    acumulador += numero
    i += 1

promedio = acumulador / 5
print(promedio)
