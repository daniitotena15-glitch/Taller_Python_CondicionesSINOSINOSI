
print ("Este programa muestra si la nota definitiva de un estudiante cumple con las condiciones y si su nota es Insuficiente, Aceptable, Sobresaliente o Excelente")
print()
notaDef= float(input("Por favor ingrese la nota defenitiva: "))

if notaDef<0 or notaDef>5.0:
    print ("Su nota es Invalida")
else:
    if notaDef<3.0:
        print ("Su Nota es Insuficiente")
    else:
        if notaDef<= 3.5:
            print ("Su nota es Aceptable")
        else:
            if notaDef<4.0:
                print ("Su nota es Sobresaliente")
            else:
                if notaDef<= 5.0:
                    print ("Su nota es Excelente")