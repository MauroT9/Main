#Realizar un programa que a partir del ingreso del importe de una compra, aplique un
#25% de descuento. Mostrar por pantalla cuánto es el total a pagar y cuánto fue el
#descuento obtenido.

importe_compra = float(input("Ingrese su importe de compra: "))

descuento = importe_compra * 0.25
total = importe_compra - descuento

print(f"El total a pagar es de {total} y el descuento fue de {descuento}")
