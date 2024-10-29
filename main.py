#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543

#Ingrese numero: 241
#142
number = (int)(input("Insert a number of three digits: "))
digit1 = number//100 
Digit2 = (number//10)%10
Digit3 = number%10
numberInvert = (Digit3*100)+(Digit2*10)+digit1
print(numberInvert)
