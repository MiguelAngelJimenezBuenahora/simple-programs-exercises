#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5
import math
radio = (float)(input("Insert the radius to circle: "))
print(f"""Perimetro: {round((2*(math.pi)*radio),1)}
Área: {round(((math.pi)*(radio*radio)),1)}""")