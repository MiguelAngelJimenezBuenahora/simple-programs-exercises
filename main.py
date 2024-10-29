#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras:

#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267
import math

CatetoA = (int)(input('Please insert the lenght "a" of the triangle: '))
CatetoB = (int)(input('Please insert the lenght "b" of the triangle: '))
print(f"""La hipotenusa es {math.hypot(CatetoA,CatetoB)}""")
