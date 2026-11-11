
print ("Este programa calcula si la llave de un tanque de agua debe estar Abierta o Cerrada segun el rango establecido ")
print ()
litro = float (input("Por favor ingrese el litraje que tiene el tanque: "))

if litro>= 250 and litro <= 450:
    print ("El tanque cumple con las condiciones del litraje establecido, por favor CIERRE la llave ")
elif litro< 250:
    falta= 250-litro
    print("El tanque NO cumple con las condiciones de litraje establecido por favor ABRA la llave ", falta, "litros para alcanzar el nivel minimo ")
else:
    print("El numero de litraje ingresado NO cumple con el ramgo establecido, esta superando el limite  CIERRA la llave")