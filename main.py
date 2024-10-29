#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5

#Ingrese un numero: -1.19
#0.19
realNumber = (float)(input("Please insert a number: "))
if realNumber < 0:
    numberfordecimal= realNumber*-1
print(round((numberfordecimal-(int(numberfordecimal))),2))