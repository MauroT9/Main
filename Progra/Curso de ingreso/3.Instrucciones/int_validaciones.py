#Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
#Los datos requeridos son:
#Apellido
#Edad, entre 18 y 90 años inclusive.
#Estado civil: "Soltero/a", "Casado/a", "Divorciado/a" o "Viudo/a".
#Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
#Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = input("Ingrese su apellido: ")

edad = int(input("Ingrese su edad: "))
while edad < 18 or edad > 90:
    edad = int(input("Reingrese su edad: "))

estado_civil = input("Ingrese su estado civil: (Soltero/a, Casado/a, Divorciado/a o Viudo/a)")
while estado_civil != "Soltero" and estado_civil != "Casado" and estado_civil != "Divorciado" and estado_civil != "Viudo":
    estado_civil = input("Reingrese su estado civil: ")

legajo = input("Ingrese su número de legajo (4 dígitos): ")
while not legajo.isdigit() or len(legajo) != 4:
    legajo = input("Reingrese su número de legajo (4 dígitos): ")    

print(f"Su apellido es: {apellido}") 
print(f"su edad es: {edad}")
print(f"su estado civil es: {estado_civil}")
print(f"Su número de legajo es: {legajo}")
