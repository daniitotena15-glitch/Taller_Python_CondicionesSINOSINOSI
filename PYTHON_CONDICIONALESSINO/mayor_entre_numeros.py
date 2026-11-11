
print("Este programa calcula y determina el numero mayor entre cuatro posibles numeros ingresados al sistema")
print ()
num1 = float (input("Por favor ingrese el primer numero: "))
num2 = float (input("Por favor ingrese el segundo numero: "))
num3 = float (input("Por favor ingrese el tercer numero: "))
num4 = float (input("Por favor ingrese el cuarto numero: "))

if num1>num2 and num1>num3 and num1>num4:
    print ("El numero mayor es el primer numero ingresado: ", num1)
else:
    if num2>num3 and num2>num4:
        print ("El numero mayor es el segundo numero ingresaDO: ", num2)
    else:
        if num3>num4:
            print ("El numero mayor es el tercer numero ingresado: ", num3)
        else:
            print("El numero mayor es el cuarto numero ingresado: ", num4)

