#Permitir que el usuario ingrese todos los números que desee.
#Los mismos deben estar comprendidos entre -10000 y 10000, y deben ser distintos de 0.
#Determinar:
#a.La suma acumulada de los números negativos. 
#b.La suma acumulada de los números positivos. 
#c.La cantidad de números negativos ingresados. 
#d.El promedio de los números positivos.
#e.El número positivo más grande.
#f.El porcentaje de números negativos ingresados, respecto del total de ingresos.

acumulador_negativos = 0
acumulador_positivos = 0
contador_negativos = 0
contador_positivos = 0
numero_positivo_mas_grande = -10001

seguir = "si"

while seguir == "si":
    numero = int(input("Ingrese un número entero entre -10000 y 10000 (distinto de 0): "))
    
    while numero == 0 or numero < -10000 or numero > 10000:
        print("Número inválido. Ingrese un número entre -10000 y 10000 (distinto de 0):")
        numero = int(input())

    if numero < 0:
        acumulador_negativos += numero
        contador_negativos += 1
    else:
        acumulador_positivos += numero
        contador_positivos += 1
        if numero > numero_positivo_mas_grande:
            numero_positivo_mas_grande = numero

    seguir = input("Ingresa otro? si/no ").lower()

promedio_positivos = acumulador_positivos / contador_positivos
porcentaje_negativos = (contador_negativos / (contador_negativos + contador_positivos)) * 100

print(f"Suma acumulada de negativos: {acumulador_negativos}")
print(f"Suma acumulada de positivos: {acumulador_positivos}")
print(f"Cantidad de negativos: {contador_negativos}")
print(f"Promedio de positivos: {promedio_positivos}")
print(f"Número positivo más grande: {numero_positivo_mas_grande}")
print(f"Porcentaje de números negativos: {porcentaje_negativos:.2f}%")