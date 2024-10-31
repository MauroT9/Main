#7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
#Calcular la suma de los números positivos y el producto de los negativos.

bandera = True
acumulador_positivos = 0
producto_negativos = 1
bandera_negativo = False
i = 0

while bandera == True:
    numero = int(input("Ingrese un numero: "))
    seguir = input("Desea continuar (si / no): ")

    if numero > 0:
        acumulador_positivos += numero
    else:
        if numero < 0:
            bandera_negativo = True
            producto_negativos *= numero

    i += 1
    if seguir == "no":
        bandera = False


print(f"La suma de los positivos es: {acumulador_positivos}")

if bandera_negativo == True:
    print(f"El producto de los negativos es: {producto_negativos}")
else:
    print(f"No se ingresaron numeros negativos: ")
