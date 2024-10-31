#Pedirle al usuario su edad, determinar si el usuario NO es adolescente.

edad = int(input("Ingrese una edad: "))

if edad < 13 or edad > 17:
    print("Usted NO es adolescente")