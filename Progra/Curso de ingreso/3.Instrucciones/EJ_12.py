#Pedir al usuario el ingreso de una nota. 
#La misma debe estar comprendida entre 1 y 10 inclusive.

nota = int(input("Ingrese la nota: "))

while not(nota >= 1 or nota <= 10):
    nota = int(input("Reingrese la nota: "))

