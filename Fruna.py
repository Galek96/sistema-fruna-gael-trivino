inventario = []
continuar = True

print("--- BIENVENIDO AL SISTEMA FRUNA ---")

while continuar == True:

    nombre = input("Ingrese el nombre del producto: ")

    while nombre == "" or nombre.isdigit() == True:
        print("Error: El nombre debe ser un texto valido.")
        nombre = input("Ingrese el nombre del producto: ")

    precio_texto = input("Ingrese el precio del producto: ")
    while precio_texto.replace(".", "", 1).isdigit() == False:
        print("Error: Debe ingresar un numero valido para el precio.")
        precio_texto = input("Ingrese el precio del producto: ")
        
    precio = float(precio_texto)

    producto = {"nombre": nombre, "precio": precio}

    inventario = inventario + [producto]

    repeticion = True

    while repeticion == True:
        comando = input("¿Desea agregar otro producto? (aparte/ahinomas): ")
        
        if comando == "aparte":
            repeticion = False
        elif comando == "ahinomas":
            repeticion = False
            continuar = False
        else:
            print("Error: El sistema no reconoce la palabra '" + comando + "'.")

print("\n==============================")
print("   RESUMEN DE COMPRA")
print("==============================")

total = 0

for prod in inventario:
    print("- " + prod["nombre"] + ": $" + str(prod["precio"]))
    total = total + prod["precio"]

print("------------------------------")
print("TOTAL A PAGAR: $" + str(total))
print("==============================")