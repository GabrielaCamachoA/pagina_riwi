#Ejercicio 10
""" palabra_palindromo = input("Ingrese una palabra: ")
for letra in palabra_palindromo[::-1]:
    if palabra_palindromo == palabra_palindromo [::-1]:
        print("La palabra ingresada si es palíndroma")
    else:
        print(f"La palabra ingresada no es palíndroma: {palabra_palindromo}")
    break """

#Ejercicio 4
""" nueva_lista = []
usuarios_registrados = ("ana", "luis", "maria", "carlos")
usuarios_nuevos = ["pedro", "ana", "maria", "sofia", "lucas", "Luis"]
for i in usuarios_registrados:
    for j in usuarios_nuevos:
        ususario = j.lower()
        if i != ususario:
            continue
        nueva_lista.append(i)
print(f"Los nombres repetidos son: {nueva_lista}") """

#Ejercicio 9
palabras = ["casa", "ordenador", "mesa", "código123", "sol", "ventilador", "mouse", "teclado", "pantalla7"]
for palabra in palabras:
    if palabra.isdigit():
        continue
    elif len(palabra) > 6:
        print(palabra)

print("Se encontraron 3 palabras que contienen más de 6 letras")
  