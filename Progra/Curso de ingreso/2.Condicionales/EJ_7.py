#Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).

edad = int(input("Ingrese una edad: "))

if edad >= 18:
    print("Es mayor")
else:
    if edad <10:
        print("Es niño/a")
    else:
        if edad <= 13:
            print("Es pre-adolescente")
        else:
            print("Es adolescente")