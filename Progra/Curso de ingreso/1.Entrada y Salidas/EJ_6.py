#Realizar un programa que pida dos números enteros. Calcular y mostrar el resto de
#la división entre ambos números. Ej: "El resto de dividir 7 por 2 es: 1"

numero_uno = int(input("Ingrese un número: "))
numero_dos = int(input("Ingrese otro número: "))

resto = numero_uno % numero_dos

print(f"El resto de dividir {numero_uno} por {numero_dos} es {resto}")
