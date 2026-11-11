
print ("")
print ()
num= int (input("Por favor ingrese el numero al cual quiere clacular si pertenece a los rangos que definira : "))
print ()
a1= int (input("Ingrese el limite inferior del primer intervalo : "))
print ()
a2= int (input("Ingrese el limite superior del primer intervalo : "))
print ()
b1= int (input("Ingrese el limite inferior del segundo intervalo : "))
print ()
b2= int (input("Ingrese el limite superior del segundo intervalo : "))
print ()
c1= int (input("Ingrese el limite inferior del tercer intervalo : "))
print ()
c2= int (input("Ingrese el limite superior del tercer intervalo : "))
print ()

if (num> a1 and num <a2) or (num >b1 and num< b2) or (num>c1 and num < c2):
    print ("El numero esta dentro de uno de los intervalos")
    print ()
else:
    print ("El numero esta fuera de los intervalos")
    print()