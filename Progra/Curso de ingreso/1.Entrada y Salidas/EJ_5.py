#Realizar un programa que permita el ingreso de dos números. Calcular la suma,
#resta, multiplicación y división de los mismos. Mostrar los resultados por pantalla.
#Utilizar una variable para mostrar el resultado (concatenar).

numero_uno = float(input("Ingrese un número: "))
numero_dos = float(input("Ingrese otro número: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
division = numero_uno / numero_dos

mensaje = f"La suma de los dos numeros es: {suma}\n"
mensaje += f"La resta de los dos numeros es: {resta}\n"
mensaje += f"La multiplicacion de los dos numeros es: {multiplicacion}\n"
mensaje += f"La division de los dos numeros es: {division}\n"

print(mensaje)
