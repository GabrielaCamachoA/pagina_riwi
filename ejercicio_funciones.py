#Recetas de cocina
#Asistente virtual de cocina que prepare las siguientes recetas:
#Ensalada César con pollo
#Wrap de pollo con salsa César
#Sándwich clásico con pollo

""" print("Bienvenido a nuestro restaurante FitGaby")
print("-" *10)
print("Este es nuetro menu:")
print("1. Ensalada César con pollo")
print("2. Wrap de pollo con salsa César")
print("3. Sándwich clásico con pollo")
orden_usuario = input("Que desea ordenar?") """
def preparar_pollo_a_la_plancha(presentacion):
    if presentacion == "tiras":
        print("La presentación del pollo seŕa en tiras")
    elif presentacion == "normal":
        print("La presentación del pollo será normal")
    return "La presentación no esta dentro de las opciones"

def preparar_salsa_cesar(pimenta_negra_molida):
    pimenta_negra_molida 
def preparar_ensalada_cesar(): 
    ingredientes_ensalada = ("lechuga", "pechuga de pollo", "cubos de pan", "queso", "aceite", "pimenton")
    presentacion_pollo = preparar_pollo_a_la_plancha("normal")
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
        "salsa" : "salsa",
        "presentacion_pollo" : presentacion_pollo,
        "ingredientes" : ingredientes_ensalada,
        "pasos" : preparacion
    }
    return receta

def preparar_wrap_cesar():
    ingredientes_wrap = ("pechugas de pollo", "tortillas de harina", "tomates cherry", "pepinos", "sal") 
    presentacion_pollo = preparar_pollo_a_la_plancha("tiras")
    preparacion = {
        "paso1" : "Sazona las pechugas con la salsa de ajo y cocinalas en una sartén o a la parrilla. ",
        "paso2" : "Coloca una tortilla en una superficie plana y sobre esta, pon una hoja de lechuga, tomates, pepino y pollo",
        "paso3" : "Baña con aderezo caesar y agrega topping para ensalada caesar y enrolla para formar el wrap. ",
        "paso4" : "Sirve el wrap con tu aderezo favorito. "
    }
    receta = {
        "receta" : "Wrap de pollo con salsa César",
        "salsa" : "salsa",
        "presentacion_pollo" : presentacion_pollo,
        "ingredientes" : ingredientes_wrap ,
        "pasos" : preparacion
    }
    return receta

def preparar_sandwich_pollo(): 
    ingredientes_sandwich = ("pechugas de pollo", "pan", "cebolla roja", "tomate grande", "ajo")
    presentacion_pollo = preparar_pollo_a_la_plancha("tiras")
    preparacion = {
        "paso1" : "Cocinar el pollo ",
        "paso2" : "Preparar los vegetales",
        "paso3" : "Mezclar el pollo",
        "paso4" : "Esamblar el sandwich"
    }
    receta = {
        "receta" : "Sándwich clásico con pollo",
        "salsa" : "salsa",
        "presentacion_pollo" : presentacion_pollo,
        "ingredientes" : ingredientes_sandwich,
        "pasos" : preparacion
    }
    return receta