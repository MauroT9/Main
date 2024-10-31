#10. Pedir el ingreso de una clave(111). Validar que el ingreso del usuario sea correcto. 
#Solo tendrá 3 intentos.

contador_intentos = 0

clave = int(input("Ingrese su clave: "))

while clave != 111 and contador_intentos < 2:
    clave = int(input("Reingrese su clave: "))
    contador_intentos += 1
    
if clave == 111:
    print("Ingresaste")
else:
    print("No ingreso")