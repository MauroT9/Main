#Integrador cometa
lado_menor= 5 
diagonal_menor = 6 
lado_mayor = 8 

#Calculo del perímetro
perimetro = (lado_menor + lado_mayor) * 2

#Aplico pitagoras para obterner la diagonal mayor
altura_BE = (lado_menor ** 2 - (diagonal_menor/2) ** 2) ** 0.5
altura_EA = (lado_mayor ** 2 - (diagonal_menor/2) ** 2) ** 0.5
diagonal_mayor = altura_BE + altura_EA

#Cantidad de varillas (en CM)
varillas_cms = perimetro + diagonal_mayor + diagonal_menor

#Cantidad del papel en cms : Area del rombo (diagonal mayor * diagonal menor)/2
area_cometa = (diagonal_mayor * diagonal_menor) / 2
cola_cometa = area_cometa * 0.1
papel_cms = area_cometa + cola_cometa

#Convertir a metros
varillas_mts = varillas_cms / 100
papel_mts = papel_cms / 100

#Materiales para 10 cometas
varillas_x10 = varillas_mts * 10
papel_x10 = papel_mts * 10

print(f"Se necesitan {round(varillas_x10, 2)} mts lineales de varillas y {round(papel_x10, 2)} metros cuadrados de papel")
