#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
#Ingrese longitud: 45
#45 cm = 17.7165 in

#Ingrese longitud: 13
#13 cm = 5.1181 in

length = (float)(input("Please insert the lenght on cm to convert to in: "))
print(f"""{length} cm = {round((length/2.54),4)} in""")


