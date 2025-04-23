#Ejercicio int
""" numero = input("Ingresa un numero: ")
if numero.isdigit():
    numero_convertido = int(numero)
    print("Seguir")
else:
    print("error") """

#Ejercicio float
""" cadena = "23.786"
cadena_convertida_a_float = float(cadena)
print(cadena_convertida_a_float)
print(type(cadena_convertida_a_float).__name__) """

#Ejrcicio str
""" name = input("Ingrese su nombre, por favor: ")
num_letras = len(name)
print(f"El nombre ingresado tiene {num_letras} letras") """

#Ejercicio bool
""" comparacion_entre_numeros = (45 < 4) and (23 > 5)
print(comparacion_entre_numeros)
print(type(comparacion_entre_numeros).__name__) """

#Ejericio 1
""" print("Suma de dos numeros")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = num1 + num2
print(f"El resultado es: {suma}") """

#Ejercicio 2
""" print("Operaciones")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = num1 + num2
resta = num1 - num2 
mult = num1 * num2
div = num1 / num2
print(f"El resultado es: {suma, resta, mult, div}") """

#Ejericio 6
""" print("Pide dos números y muestra si son iguales, o cuál es mayor.")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 == num2:
    print("Los numeros ingresados son iguales")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}") """

#Ejercicio 7
""" num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > 10 and num2 > 10:
    print("Los numeros son mayores que 10")
elif num1 > 10 or num2 > 10:
    print("Un numero es mayor que 10")
else:
    print("Ninguno de los numeros es mayor que 10") """