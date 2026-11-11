
print ("Este programa calcula si un articulo cumple con una condicion el el precio para poder brindar un descuento del 5%")
print ()
arti = float (input("Por favor ingrese el precio del articulo: "))
print ()

if arti>150000:
    descu= arti*0.05
    total= arti-descu
    print()
    print ("El articulo es superior al tope establecido y es apto para continuar con el descuento del 5 porciento ")
    print ()
    print (f"Felicitaciones, su total a pagar es de: ${total:.2%} ,  ${total:,.2f} ")
    print ()
else:
    print ("Su compra NO cumple con el tope establecido para adquirir el descuento :3")
    print()
    print (f"Lo sentimos sera para tu proxama compra, sigue intentando, su total a pagar es de: ${arti:,.2f}")
