
print ("Este programa calcula y determina si un numero X, se encuentra en el rango que se ingresa al sistema")
print ()

rango1= float(input("Por favor ingrese el numero desde donde se va a tomar el rango (Recuerda este valor se tomara en cuenta): "))
rango2= float(input("Por favor ingrese el numero desde donde se va a tomar el rango (Recuerda este valor se tomara en cuenta): "))
num = float (input("Ingrese el numero el cual se debe calcular si se encuentra en el rango establecido: "))
if num<=rango1 and num<=rango2:
    print ("Su numero NO se encuentra en el rango establecido")
else:
    print ("Su numero se encuentra en el rango establecido")
