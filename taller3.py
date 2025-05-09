#crear un programa en Python que permita al equipo 
# añadir, consultar, actualizar y eliminar productos del inventario de manera eficiente,
# así como calcular el valor total del inventario.

productos = []

def añadir_producto(nombre_producto, precio, cantidad):
    while True:
        try:
            nombre_producto = input("Nombre del producto: ").lower()
            precio = int(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            print("-" * 20)
            productos.append({
                "nombre": nombre_producto, 
                "precio": precio,
                "cantidad" :cantidad}) 
            break
        except ValueError:
            print("Error. Ingresa valores válidos")

def buscar_producto():
    while True:
        try:
            producto_a_buscar = input("Ingrese el nombre del producto que desea buscar? -> ")
            for clave in productos:
                if clave["nombre"] == producto_a_buscar.lower():
                    print("\nProducto encontrado")
                    print("-" * 20)
                    print(clave["nombre"])
                    print(f"Precio: {clave['precio']} Cantidad: {clave['cantidad']}")
                    return clave["nombre"]
                else:
                    print("Producto no encontrado")
            break
        except ValueError:
            print("Ingresa valores válidos")    

def actualizar_precio():
    producto_a_buscar = input("Ingrese el nombre del producto a actualizar: ").lower()
    for producto in productos:
        if producto["nombre"] == producto_a_buscar:
            while True:
                try:
                    nuevo_precio = float(input(f"\nIngresa el nuevo precio del producto '{producto_a_buscar}' -> "))
                    producto["precio"] = nuevo_precio
                    print(f"Precio actualizado a: {producto['precio']}")
                    return
                except ValueError:
                    print("Ingrese un valor válido numérico")
    print("Producto no encontrado para actualizar.")

def ver_productos():
    for producto in productos:
        print(producto)

def eliminar_producto():
    ver_productos()
    product = input("Ingresa el nombre del producto que deseas eliminar: ")

    for i, producto in enumerate(productos):
        if producto["nombre"] == product:
            producto_eliminado = productos.pop(i)
            print(f"Producto eliminado: {producto_eliminado}")
            return
    else:
        print(f"El producto {product} no fue encotrado")

def menu():
    opciones = {
    "1": "Añadir producto",
    "2" : "Buscar producto",
    "3" : "Actualizar precio",
    "4" : "Eliminar producto"
    }
    for clave,valor in opciones.items():
        print(f"{clave}: {valor}")
    print("-" * 20)
    while True:
        try:
            seleccion_usuario = input("Elige una de las opciones: ")
            if seleccion_usuario not in opciones:
                print("No esta dentro de las opciones")
                seleccion_usuario = input("Elige una una de las opciones: ") # mejora
            match seleccion_usuario:
                case "1":
                    añadir_producto(nombre_producto=productos, precio=productos, cantidad=productos)
                case "2":
                    buscar_producto()
                case "3":
                    actualizar_precio()
                case "4":
                    eliminar_producto()
            break
        except ValueError:
            print("Error. Ingresa valores válidos")

print("Bienvenido, que desea hacer en el inventario en el día de hoy?")
menu()
while True:   
    try:
        repetir = input("\nQuieres seguir en el programa?  Y/N: ").lower()
        if repetir == "y":
            menu()
        elif repetir == "n":
            print("Vuelva pronto!!")
            break
        else:
            print("Ingresa la letra correcta")
    except ValueError:
        print("Ingresa 'y' o 'n' ")
