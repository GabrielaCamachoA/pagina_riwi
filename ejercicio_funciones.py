#Asistente virtual de cocina que prepare las siguientes recetas: Ensalada César con pollo, Wrap de pollo con salsa César y
#Sándwich clásico con pollo

#Funcion para la presentacion del pollo
def preparar_pollo_a_la_plancha(presentacion):
    if presentacion == "tiras":
        print("\nLa presentación del pollo será en tiras")
        return
    elif presentacion == "normal":
        print("\nLa presentación del pollo será normal")
        return
    return "La presentación no esta dentro de las opciones"

#Funcion para verificar si el usuario desea pimienta salsa
def preparar_salsa_cesar(pimenta_negra_molida):
    if pimenta_negra_molida == "s":
        print("\nSe le agregara pimienta a su salsa")
    else:
        print("\nNo se le agregara pimienta a su salsa")
        return pimenta_negra_molida

#Funciones para los distintos platos (de la linea 21 hasta la 78)
def preparar_ensalada_cesar(salsa, presentacion_pollo): 
    ingredientes_ensalada = ("lechuga", "pechuga de pollo", "cubos de pan", "queso", "aceite", "pimenton")
    salsa = preparar_salsa_cesar(pimenta_negra_molida=salsa)
    presentacion_pollo = preparar_pollo_a_la_plancha(presentacion=presentacion_pollo)
    preparacion = {
        "paso1" : "Para el aliño, poner todos los ingredientes menos el aceite en una licuadora.",
        "paso2" : "Con la licuadora andando al mínimo, agregar de a poco el aceite de oliva para tener una mezcla emulsionada y espesa.",
        "paso3" : "Sazonar con sal de mar gourmet y pimienta blanca molida gourmet.",
        "paso4" : "Calentar el horno a 200°C.",
        "paso5" : "Mezclar el pan con el aceite de oliva y con el pimentón páprika.",
        "paso6" : "Hornear por 3 a 5 minutos o hasta que el pan esté crujiente y dorado.",
        "paso7" : "Hornear por 3 a 5 minutos o hasta que el pan esté crujiente y dorado."
    }
    receta = {
        "receta" : "Ensalada César con pollo",
        "salsa" : salsa,
        "presentacion_pollo" : presentacion_pollo,
        "ingredientes" : ingredientes_ensalada,
        "pasos" : preparacion
    }
    return receta

def preparar_wrap_cesar(salsa, presentacion_pollo):
    ingredientes_wrap = ("pechugas de pollo", "tortillas de harina", "tomates cherry", "pepinos", "sal") 
    salsa = preparar_salsa_cesar(pimenta_negra_molida=salsa)
    presentacion_pollo = preparar_pollo_a_la_plancha(presentacion=presentacion_pollo)
    preparacion = {
        "paso1" : "Sazona las pechugas con la salsa de ajo y cocinalas en una sartén o a la parrilla. ",
        "paso2" : "Coloca una tortilla en una superficie plana y sobre esta, pon una hoja de lechuga, tomates, pepino y pollo",
        "paso3" : "Baña con aderezo caesar y agrega topping para ensalada caesar y enrolla para formar el wrap. ",
        "paso4" : "Sirve el wrap con tu aderezo favorito. "
    }
    receta = {
        "receta" : "Wrap de pollo con salsa César",
        "salsa" : salsa,
        "presentacion_pollo" : presentacion_pollo,
        "ingredientes" : ingredientes_wrap ,
        "pasos" : preparacion
    }
    return receta

def preparar_sandwich_pollo(presentacion_pollo): 
    ingredientes_sandwich = ("pechugas de pollo", "pan", "cebolla roja", "tomate grande", "ajo")
    presentacion_pollo = preparar_pollo_a_la_plancha(presentacion=presentacion_pollo)
    preparacion = {
        "paso1" : "Cocinar el pollo ",
        "paso2" : "Preparar los vegetales",
        "paso3" : "Mezclar el pollo",
        "paso4" : "Esamblar el sándwich"
    }
    receta = {
        "receta" : "Sándwich clásico con pollo",
        "salsa" : "salsa",
        "presentacion_pollo" : presentacion_pollo,
        "ingredientes" : ingredientes_sandwich,
        "pasos" : preparacion
    }
    return receta

#Funcion encargada para retornar las recetas de los platos
def emplatado(receta):
    return receta


#Funcion principal donde le damos la bienvenida al ususario y le preguntamos que desea ordenar
print("Bienvenido a restaurante FitGaby")
def restaurante_fitgaby():
    plato = input("Que plato desea ordenar? (Ensalada César con pollo, Wrap de pollo con salsa César y Sándwich clásico con pollo): ").lower()
    presentacion_pollo = input("\n Como desea la presentacion del pollo? Tiras/Normal: ").lower()

    if plato == "ensalada César con pollo" or plato == "ensalada" or plato == "ensalda con pollo":
        salsa = input("Desea agregarle pimienta a su salsa? S/N: ").lower()
        receta_preparada = preparar_ensalada_cesar(salsa, presentacion_pollo)
    elif plato == "wrap de pollo con salsa cesar" or plato == "wrap de pollo":
        salsa = input("Desea agregarle pimienta a su salsa? S/N: ").lower()
        receta_preparada = preparar_wrap_cesar(salsa, presentacion_pollo)
    elif plato == "sandwich clasico con pollo" or plato == "sandiwch con pollo" or plato == "sandwich":
        receta_preparada = preparar_sandwich_pollo(presentacion_pollo)
    else:
        return print("Esa opcion no se encuentra en nuestro menu")
    plato = emplatado(receta_preparada)
    print("\nReceta del plato: ")
    print(plato)
restaurante_fitgaby()