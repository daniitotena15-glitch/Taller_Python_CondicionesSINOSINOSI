
print ("Este programa determina si un numero real N, se encuentra en un uno de los siguientes rangos: (3,5  7,8] , [9,3 4,5) y [23,4 45,3]")
print ()
num= float (input("Por favor ingrese un numero: "))

if (num>3.5 and num<= 7.8) or (num>= 9.3 and num> 4.5) or (num>=23.4 and num<=45.3):
    print ("El numero ingresado esta en el rango establecido")
else:
    print ("El numero ingresado NO esta en el rango por favor intente con otro numero")