#Ejercicio 1
""" numero = int(input("Ingrese un numero: "))
if numero > 0 and  numero % 2 == 0:
    print("El numero es postivo y par") 
elif numero % 2 == 1:
        print("El numero positivo y es impar")
elif numero < 0 and numero % 2 == 0:
    print("El numero es negativo y par")
elif numero % 2 == 1:
     print("El numero negativo y es impar")
else:
    print("El numero es 0") """

#Ejercicio 2
""" edad = int(input("Ingrese su edad: "))
if edad > 65:
    print("Adulto mayor")
elif edad >= 31:
    print("Adulto maduro")
elif edad >= 18:
    print("Adulto joven")
else:
    print("Menor de edad") """

#Ejercio 3
""" dia_laborable = input("El día es laborable? (S/N): ")
if dia_laborable == "S" or dia_laborable == "s":
    hora_del_dia = int(input("Ingresa la hora del día en forma militar (0-23): "))
    if hora_del_dia >= 7 and hora_del_dia <= 9 and hora_del_dia >= 17 and hora_del_dia <= 19:
        print("Pico")
    else:
        print("Normal")
elif dia_laborable == "N" or dia_laborable == "n":
    print("Fin de semana")
else:
    print("Ingresa un valor valido") """

#Ejercicio 4
""" monto_de_compra = int(input("Ingrese el monto de su compra: "))
vip = input("Es VIP? (S/N)").lower()
while vip == "s":
    if monto_de_compra >= 500:
        descuento = monto_de_compra * 0.20
        print(f"El descuento aplicado es del 20% y queda en: {descuento:,.2f}")
    else:
        descuento = monto_de_compra * 0.10
        print(f"El descuento aplicado es del 10% y queda en: {descuento:,.2f}")
    break
else:
    if monto_de_compra >= 500:
        descuento = monto_de_compra * 0.5
        print(f"El descuento aplicado es del 5% y queda en: {descuento:,.2f}")
    else:
        print("No hay descuento aplicado") """

#Ejercicio 5
contraseña = input("Crear contraseña: ")
requisito = "@"
while len(contraseña) != 8 and requisito not in contraseña:
    print("La contraseña debe tener 8 caracteres y contener al menos el caracter @")
    contraseña = input("Crear contraseña: ")
    if len(contraseña) < 8 and requisito in contraseña:
        print("La contraseña debe tener 8 caracteres")
        contraseña = input("Crear contraseña: ")
else:
    print("Contraseña valida")