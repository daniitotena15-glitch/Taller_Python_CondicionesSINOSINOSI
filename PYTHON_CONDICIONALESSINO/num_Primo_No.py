
print ("Este programa determina si el numero ingresado de un rango de 0 a 20 es un numero primo o no")
print ()
num = int (input("Por favor ingrese el numero: "))
if num >=0 and num>=20:
    print()
    print ("El numero ingresado NO se encuentra en el rango establecido , por favor reinicia el programa e intenta nuevamente")
    print ()
elif num== 2 or num==3  or num==5 or num==7 or num==11 or num==13 or num==17 or num==19:
    print ("El numero ingresado es primo: ", num)
else:
    print ("El numero ingresado NO es primo: ", num)
