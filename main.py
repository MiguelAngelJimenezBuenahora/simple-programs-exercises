#Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando la temperatura sobrepasa un punto crítico. A medida que la temperatura aumenta, las reacciones se aceleran.

#En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema lo hacen para temperaturas sobre 70°C. Para hacer un huevo a la copa, la clara debe haber sido calentada lo suficiente para coagularse a más de 63°C, pero la yema no debe sobrepasar los 70°C para evitar obtener un huevo duro.

#El tiempo en segundos que toma al centro de la yema alcanzar Ty

#°C está dado por la fórmula:
#t=M2/3cρ1/3Kπ2(4π/3)2/3ln[0.76To−TwTy−Tw],

#donde M
#es la masa del huevo, ρ su densidad, c su capacidad calorífica específica y K

#su conductividad térmica. Algunos valores típicos son:

 #   M=47[g]

#para un huevo pequeño y M=67[g]
#para uno grande,
#ρ=1.038[gcm−3]
#,
#c=3.7[Jg−1K−1]
#, y
#K=5.4⋅10−3[Wcm−1K−1

#   ].

#Tw
#es la temperatura de ebullición del agua y To

#la temperatura original del huevo antes de meterlo al agua, ambos en grados Celsius.

#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

import math
TempOrigEgg = (float)(input("Please insert the original temp of the egg: "))
MofEggSmall = 47
MofEggBig = 67
P = 1.038   #Densidad
c = 3.7     #Capacidad calorifica especifica
k = 5.4**-3 #Conductividad térmica
Tw = 100    #
Ty = 70     #Temperatura final de la yema
print(f"""El tiempo que tarda en alcanzar la temperatura máxima son:
       Si es un huevo pequeño {int(((MofEggSmall**(2/3)*c*P**(1/3))/(k*math.pi**2)*(((4*math.pi)/3)**(2/3))*(math.log(0.76*((TempOrigEgg-Tw)/(Ty-Tw))))))} segundos. 
       Si es un huevo grande {int(((MofEggBig**(2/3)*c*P**(1/3))/(k*math.pi**2)*(((4*math.pi)/3)**(2/3))*(math.log(0.76*((TempOrigEgg-Tw)/(Ty-Tw))))))} segundos""")