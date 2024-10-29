#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75
import math
print("In the current text insert the 4 notes in order: ")
FirstNote = (float)(input("Insert the first note: "))
SecondNote = (float)(input("Insert the second note: "))
ThirdNote = (float)(input("Insert the third note: "))
FourNote = (float)(input("Insert the quarter note: "))
print(f"""the grade average is: {round(((FirstNote+SecondNote+ThirdNote+FourNote)/4),2)}""")
