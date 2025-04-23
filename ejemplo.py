""" import operator
operaciones = {
    "+" : operator.add,
    "-" : operator.sub
}
primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("Ingrese un numero: "))
operacion = input("Selecciona la operacion que deseas realizar: ")
resultado = operaciones[operacion](primer_numero, segundo_numero)
print(resultado) """

#Ejercicio 1
""" print("NUmero par o impar")
num = int(input("Ingrese el primer numero: "))
if num % 2 == 0:
    print ("El numero es par")
else:
    print("El numero es impar") """

#Ejercicio 2
""" print("Mayor de dos números")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el primer numero: "))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}") """

#Ejercicio 3
""" print("Edad para votar")
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Adelante, puedes votar")
else:
    print("Aún no estas apto para votar") """

#Ejercicio 4
""" print(" Número positivo, negativo o cero")
num = int(input("Ingrese el primer numero: "))
if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es igual a 0") """

#Ejercicio 5
""" print("Calificación aprobatoria")
calificacion = int(input("Ingresa la calificación: "))
if calificacion >= 60:
    print("Felicidades!! Aprobaste")
else:
    print("Sigue intentandolo!") """

#Ejercicio 6
""" print("Divisible por 5")
num = int(input("Ingrese el primer numero: "))
if num % 5 == 0:
    print("El numero es divisible por 5")
else:
    print("No es divisible por 5") """

#Ejercicio 7
""" print("Es un múltiplo de 3")
num = int(input("Ingrese el primer numero: "))
if num % 3 == 0:
    print("El numero es múltiplo de 3")
else:
    print("No es múltiplo de 3") """

#Ejercicio 8
""" print("Fecha de nacimiento y signo zodiacal")
dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento como numero: "))

if dia >= 21 and mes == 3 or dia <= 19 and mes == 4:
    print("Tu signo del zodiaco es Aries")
elif dia >= 20 and mes == 4 or dia <= 20 and mes == 5:
    print("Tu signo del zodiaco es Tauro")
elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6:
    print("Tu signo del zodiaco es Géminis")
elif dia >= 21 and mes == 6 or dia <= 22 and mes == 7:
    print("Tu signo del zodiaco es Cáncer")
elif dia >= 23 and mes == 7 or dia <= 22 and mes == 8:
    print("Tu signo del zodiaco es Leo")
elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
    print("Tu signo del zodiaco es Virgo")
elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
    print("Tu signo del zodiaco es Libra")
elif dia >= 23 and mes == 10 or dia <= 21 and  mes == 11:
    print("Tu signo del zodiaco es Escorpio")
elif dia >= 22 and mes == 11 or dia <= 21 and  mes == 12:
    print("Tu signo del zodiaco es Sagitario (el mejor!!!)")
elif dia >= 22 and mes == 12 or dia <= 19 and mes == 1:
    print("Tu signo del zodiaco es Capricornio")
elif dia >= 20 and mes == 1 or dia <= 18 and  mes == 2:
    print("Tu signo del zodiaco es Acuario")
elif dia >= 19 and mes == 2 or dia <= 20 and  mes == 3:
    print("Tu signo del zodiaco es Piscis")
else:
    print("Ingresa un valor valido") """