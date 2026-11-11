
print ("Este algoritmo determina si una ecuación cuadrática tiene solución")
print()
a= float(input("Ingrese el valor de a: "))
print()
b= float(input("Ingrese el valor de b: "))
print()
c= float(input("Ingrese el valor de c: "))

comprobra = b*b - 4*a*c

if a != 0:
    if comprobra >= 0:
        print()
        print("La ecuacion tiene solucion")
        print()
    else:
        print()
        print("Si resultado es : ", comprobra)
        print ("La ecuacion NO tiene solucion")
        print()
else:
    print()
    print ("NO es una ecuacion cuadratica")