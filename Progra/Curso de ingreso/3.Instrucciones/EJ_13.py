#Solicitarle al usuario el ingreso de un color primario. 
#Validar que el mismo sea Rojo, Verde o Azul.

color = input("Ingrese un color: ")

while color != "Rojo" and color != "Verde" and color != "Azul":
    color = input("Reingrese un color: ")

print("Ingresaste un color primario") 
