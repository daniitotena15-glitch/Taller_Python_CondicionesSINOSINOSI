
print("Este algoritmo muestra el porcentaje de descuento según el artículo seleccionado")

print()

opciones = [
    "1. Textil",
    "2. Electrodomésticos",
    "3. Elementos de cocina",
    "4. Videojuegos"
]

for op in opciones:
    print(op)

print()

selec = input("Por favor elija una opción: ")

print()

if selec == "1":
    print("Artículo: Textil")
    print("Descuento: 0%")

elif selec == "2":
    print("Artículo: Electrodomésticos")
    print("Descuento: 3.7%")

elif selec == "3":
    print("Artículo: Elementos de cocina")
    print("Descuento: 4.2%")

elif selec == "4":
    print("Artículo: Videojuegos")
    print("Descuento: 7.8%")

else:
    print("La opción seleccionada no se encuentra disponible")