""" name = "Gabriela Camacho"

for i in range (3):
    print(f"hola #{i+1}")

iterador = 0
while iterador < 5:
    print("hola", iterador)
    iterador += 1 """

""" frustas = ("pera", "mango", "manzana")
frustas_v2 ={
    "sabor": "vainilla",
    "cantidad" : "70g",
    "marca" : "mcdonalds",
    "fruta" : "fresas"
}
#Extraer la llave y el valor
for clave, valor in frustas_v2.items():
    print(f"el item es {clave} y su valor es: {valor}")
print("=" *10)
#Extraer solamente la llave
for elemento in frustas_v2:
    print(f"el item es: {elemento}")

for clave in frustas_v2.keys():
    print(f"El item es: {clave}")
print("=" *10)
#Extraer el valor
for valor in frustas_v2.values():
    print(f"El item es: {valor}") """

""" sabores = ["uva", "vainilla", "arequipe"]
for sabor in sabores:
    print(f"el sabor es: {sabor}")

for index,sabor in enumerate(sabores):
    if sabor == "vainilla":
        print(f"el sabor es #: {sabor}")
        print(index) """

#ejercicios con ciclo for
#1
#for numero in range (10):
#    print(numero)

#2
#for i in range (100, 200):
#    print(i)

#3
#for numero in range (5,21,3):
#    print(numero)

#4
#numero = int(input("Ingrese un numero: "))
#if numero > 0:
#    doble_del_numero = (2 * numero)
 #   for i in range (numero,doble_del_numero - 1):
  #      print(i)
#else:
 #   print("Ingresa un numero positivo")

#5
""" suma = 0
numero = int(input("Ingrese una cantidad: "))
for num in range (numero):
    print(num)
    numero_ingresado = int(input("Ingrese un numero: "))
    suma += numero_ingresado
    
print(f"La suma de los numeros ingresados fue: {suma}") """

#6
#lower para que toda la frase este en minuscula
""" frase = input("Ingresa una frase: ").lower()
# set() se utiliza para guardar elementos y que no esten duplicados
vocales_en_la_frase = set()
"""  """
for i in frase:
    if i in "aeiou":
        vocales_en_la_frase.add(i)
print("Se encontraron estas vocales en la frase: ")
for vocal in vocales_en_la_frase:
    print(vocal) """

#7
#frase = input("Ingresa una frase: ").lower()
#suma = 0
#for vocal in frase:
#    if vocal in "aeiou":
#        suma += 1
#print(f"Se encontraron {suma} vocales")

#8
""" suma = 0
for num in range(101):
   suma += num
print(f"La suma de todos los numeros de 0 a 100 es: {suma}") """



#Definir mi grupo de infromacion la cual estara asociada a un diccionario
#donde la clave correpondera a la cedula dd un coder. El valor asocidado a cada clave
#correspóndera al nombre completo del coder
coders = {
    1234 : "Gabriela Camacho",
    3214 : "Dylan Sanchez",
    4321 : "Andres Santoyo"
}
#Definicion de variable que actuara como bandera, su valor estara sujeto a la busqueda exitosa de un coder
flag = False

#Construccion del cilclo que permitira realizar el recorrido de cada par de elementos
#asociados al diccionario para la busqueda del coder

coder_buscado = input("Ingrese el nombre del coder a buscar: ")
for id, coder in coders.items():
    if coder_buscado.lower() in coder.lower():
        flag = True
        print(f"El Coder con nombre {coder} tiene la cédula: {id}")
else:
    print("Se ha finalizado la busqueda")
    if flag:
        print("Se encontro el coder")
    else:
        print("No se encontro el coder")