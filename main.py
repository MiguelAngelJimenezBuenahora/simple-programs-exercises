#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.
#NC=(C1+C2+C3)/3
#NF=NC⋅0.7+NL⋅0.3

#Donde NC
#es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3

nFirstCertamen = (int)(input("Please insert the score of the first certamen: "))
nSecondCertamen = (int)(input("Please insert the score of the second certamen: "))
nl= (int)(input("please insert the score of the laboratory: "))

nc = ((60 - nl * 0.3) / 0.7)
print(f"""Need a score of {((int)(3*nc-nFirstCertamen-nSecondCertamen))} in the third certamen for pass in NF with 60""")