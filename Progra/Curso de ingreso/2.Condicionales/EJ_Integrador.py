# Ferrete Lámparas

# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de # lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.
# A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente # descuento:
# Si compra 6 o más lámparas bajo consumo tiene un descuento del 50%.
# Si compra 5 lámparas bajo consumo marca "Argentina Luz" se hace un descuento del 40% y si es de otra marca el descuento es # del 30%.
# Si compra 4 lámparas bajo consumo marca "Argentina Luz" o "FelipeLamparas" se hace un descuento del 25 % y si es de otra marca # el descuento es del 20%.
# Si compra 3 lámparas bajo consumo marca "Argentina Luz" el descuento es del 15%, si es "FelipeLamparas" se hace un descuento # del 10 % y si es de otra marca un 5%.
# Por otro lado, si el importe final con descuento suma más de $4000 se obtiene un descuento adicional de 5%.
# Mostrar por pantalla:
# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si # corresponde) y el total a pagar con descuento.

marca = input("Ingrese marca ")
cantidad = int(input("Ingrese la cantidad "))

precio = 800
porcentaje = 0
adicional = 0

subtotal = cantidad * precio

mensaje = f"Marca: {marca}\n"    
mensaje += f"Cantidad: {cantidad}\n"
mensaje += f"Total sin descuento: {subtotal}\n"

if cantidad >= 6:
    porcentaje = 50
elif cantidad == 5:
        if marca == "ArgentinaLuz":
            porcentaje = 40
        else:
            porcentaje = 30
elif cantidad == 4:
        if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
            porcentaje = 25
        else:
            porcentaje = 20
elif cantidad == 3:
        if marca == "ArgentinaLuz":
            porcentaje = 15
        elif marca == "FelipeLamparas":
                porcentaje = 10
        else:
                porcentaje = 5

if porcentaje != 0:
    descuento = subtotal * porcentaje / 100
    mensaje += f"Descuento: {descuento}\n"                

total_con_descuento = subtotal - descuento

if total_con_descuento > 4000:
    adicional = total_con_descuento * 0.05
    total_con_descuento -= adicional
    mensaje += f"Descuento adicional: {adicional}\n"

mensaje += f"Total: {total_con_descuento}\n"  

print(mensaje)
