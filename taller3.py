#crear un programa en Python que permita al equipo 
# añadir, consultar, actualizar y eliminar productos del inventario de manera eficiente,
# así como calcular el valor total del inventario.

productos = []

def añadir_producto(nombre_producto, precio, cantidad):
    productos.append(
        {"nombre": nombre_producto, 
         "precio": precio,
        "cantidad" :cantidad}
    ) 
    while productos:
        try:
            nombre_producto = str(input("Nombre del producto: "))
            precio = int(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            
            break
        except:
            print("Error. Ingresa valores válidos")

def buscar_producto():
    nombre_a_buscar = input("Ingresa el nombre del producto que quieres buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_a_buscar.lower():
            print(f"Producto encontrado: {producto}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")



def menu():
    opciones = {
    "1": "Añadir producto",
    "2" : "Buscar producto",
    "3" : "Actualiar precio de un producto",
    "4" : "Eliminar producto"
}
    for clave,valor in opciones.items():
        print(f"{clave}: {valor}")
    print("-" * 20)
    try:
        seleccion_usuario = int(input("Elige una de las opciones: "))
        if seleccion_usuario < 1 or seleccion_usuario > 4:
            print("No esta dentro de las opcines")
            seleccion_usuario = int(input("Elige una una de las opciones: "))
        match seleccion_usuario:
            case 1:
                añadir_producto(nombre_producto=productos, precio=productos, cantidad=productos)
            case 2:
                buscar_producto()
    except:
        print("Error. Ingresa valores válidos")

print("Bienvenido, que desea hacer en el inventario en el día de hoy?")
menu()
while True:   
    try:
        repetir = input("¿Quieres seguir en el programa o despedirte?  Y/N: ").lower()
        if repetir == "y":
            menu()
        elif repetir == "n":
            print("chao")
            break
        else:
            print("Ingresa la letra correcta")
    except:
        print("Ingresa valores válidps")


""" productos = []

def añadir_producto(nombre_producto, precio, cantidad):
    try:
        productos.append({
            "nombre": nombre_producto,
            "precio": precio,
            "cantidad": cantidad
        })
        print("Producto añadido con éxito.")
    except:
        print("Error al añadir el producto.")

def buscar_producto():
    nombre_a_buscar = input("Ingresa el nombre del producto que quieres buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_a_buscar.lower():
            print(f"Producto encontrado: {producto}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def menu():
    opciones = {
        "1": "Añadir producto",
        "2": "Buscar producto",
        "3": "Actualizar precio de un producto",
        "4": "Eliminar producto"
    }

    for clave, valor in opciones.items():
        print(f"{clave}: {valor}")
    print("-" * 20)

    try:
        seleccion_usuario = int(input("Elige una de las opciones: "))
        if seleccion_usuario < 1 or seleccion_usuario > 4:
            print("No está dentro de las opciones.")
            return

        match seleccion_usuario:
            case 1:
                try:
                    nombre = input("Nombre del producto: ")
                    precio = int(input("Precio del producto: "))
                    cantidad = int(input("Cantidad del producto: "))
                    añadir_producto(nombre, precio, cantidad)
                except:
                    print("Error. Ingresa datos válidos.")
            case 2:
                buscar_producto()
            case 3:
                print("Función no implementada aún.")
            case 4:
                print("Función no implementada aún.")
    except:
        print("Error. Ingresa un número válido.")

print("Bienvenido, ¿qué desea hacer en el inventario el día de hoy?")
menu()

while True:
    repetir = input("¿Quieres seguir en el programa o despedirte?  Y/N: ").lower()
    if repetir == "y":
        menu()
    elif repetir == "n":
        print("Chao")
        break
    else:
        print("Ingresa la letra correcta") """
