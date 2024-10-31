#Pedir el ingreso de una clave (111). Validar que el ingreso del usuario sea correcto. 
#Tendrá inderterminados intentos.

clave = int(input("Ingrese su clave: "))

while clave != 111:
    clave = int(input("Reingrese su clave: "))

print("Ingresaste")
