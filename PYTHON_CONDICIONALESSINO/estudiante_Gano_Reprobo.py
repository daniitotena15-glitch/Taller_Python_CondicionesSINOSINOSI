
print ("Este programa calcula si un estudiante Gano o perdio el curso en base a la entrega de cinco Notas")

nota1= float (input("Por favor ingrese la primera nota: "))
if nota1 >= 0.0 and nota1 <= 5.0:
    nota2= float (input("Por favor ingrese la segunda nota: "))
    if nota2 >=0.0 and nota2<= 5.0:
        nota3 = float(input("Por favor ingrese la tercera nota: "))
        if nota3>= 0.0 and nota3 <= 5.0 :
            nota4 =float (input("Por favor ingrese la cuarta nota: "))
            if nota4 >=0.0 and nota4 <= 5.0:
                nota5= float(input("Por favor ingrese la quinta y ultima nota: "))
                if nota5 >=0.0 and nota5<= 5.0:
                    notaDef=(nota1+nota2+nota3+nota4+nota5)/5
                    if notaDef> 3.5:
                        print(f"Felicitaciones GANASTE el curso, tu nota definitiva es : {notaDef:.1f}")
                    else:
                        print (f"Lo siento ..., tu nota definitiva es : {notaDef}, NO lograste pasar el curso")
                else:
                    print("La nota ingresado NO es valida, por favor intente de nuevo ")
            else:
                print("La nota ingresado NO es valida, por favor intente de nuevo ")
        else:
            print("La nota ingresado NO es valida, por favor intente de nuevo ")
    else:
        print("La nota ingresado NO es valida, por favor intente de nuevo ")
else:
    print("La nota ingresado NO es valida, por favor intente de nuevo ")