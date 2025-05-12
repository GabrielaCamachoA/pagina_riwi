#manage inventory in a store
#principal functions: add, search, update and delete product + calculate total value of the inventory 

#in this variable save the list of dictionarys
products = []

#Functions with differents actions that they are going be execute
# throught the code you will find loops while for manage errors
def add_product():
    print("Introduce five products:")
    #with this for the user can add five products with price and number of products
    for product in range(5):
        name_product = input(f"Introduce the name of the product {product+1}: ")
        #this is for the user introduce a valid name
        while len(name_product) <= 2:
            print("Introduce a correct name")
            name_product = input(f"Introduce the name of the product {product+1}: ")
        while True:
            try:
                price = int(input("Introduce a price: "))
                number_of_products = int(input("Introduce how many products do you want: "))
                product = {
                    "name": name_product,
                    "price" : price,
                    "number" : number_of_products
                }
                print("-" * 20)
                #with append() the products add at the list with information
                products.append(product)
                break
            except ValueError:
                print("Please, introduce valids datas")
    #this is for ask a user if the user want add more products
    ask_user = input("Do you want add more products? (Y/N): ").lower()
    if ask_user == "y":
        name_product = input(f"Introduce the name of the product : ")
        while len(name_product) <= 2:
            print("Introduce a correct letter")
            name_product = input(f"Introduce the name of the product: ")
        else: 
            while True:
                try:
                    price = int(input("Introduce a price: "))
                    number_of_products = int(input("Introduce how many products do you want: "))
                    product = {
                        "name": name_product,
                        "price" : price,
                        "number" : number_of_products
                    }
                    print("-" * 20)
                    products.append(product)
                except ValueError:
                    print("Please, introduce valids datas")
    else:
        print("Okey")
        
            

def search_product():
    find_a_product = input("Introduce the name of the produc to search: ")
    while len(find_a_product) <= 2:
            print("Introduce a correct name")
            find_a_product = input("Introduce the name of the produc to search: ")
    else:
        #thius is for to cover and compare the name to search with the key has the list of products and show the information if both are same
        for product in products:
            if product["name"] == find_a_product:
                print("Product found")
                print(f"Name: {product['name']}")
                print("-" * 10)
                print(f"Price: {product['price']} Number: {product['number']}")  
        else:
            print("Product not found")

def update_price():
    #I call the function for to optimize code because I use the same logic in this function for update price
    product_updte = search_product()
    #it's use a for por cover products and compare the name to search with the key has the list of products and change the price
    for product in products:
        if products["name"] == product_updte:
            while True:
                try:
                    new_price = int(input(f"Introduce the new price for {product_updte}: "))
                    while new_price < 0:
                        print("Please, intoduce positive numbers")
                    product["price"] = new_price
                    print("Price update")
                    print(f"Name: {product['name']}")
                    print("-" * 10)
                    print(f"Price: {product['price']} ")
                except ValueError:
                    print("Please, introduce valids datas")
            

def delete_product():
    delete_a_product = input("Introduce the name of product to delete: ")
    #in this for I use 2 variables for cover the list of products. "i" for index and "product" for differents dictionarys in the list
    #enumerate() help us cover the list and show the position of dictionartys (product) for remove it
    for i, product in enumerate(products):
        #if the prodcut introduce for the user is find in the list will eliminate it with .pop()
        if product["name"] == delete_a_product:
            product_removed = products.pop(i)
            print(f"Product removed: {product_removed}")
            return
    else:
        print(f"The product {delete_a_product} is not found")
#function lambda for calculate total inventory
total_inventory = lambda: sum(value["price"] * value["number"] for value in products)

#function where it's will execute menu and it will be in charge to call other functions
def menu():
    options={
        "1": "Add a product",
        "2": "Search a product",
        "3": "Update price of a product",
        "4": "Delete product",
        "5": "Total inventory"
    }
    for key, value in options.items():
        print(f"{key}: {value}")
    print("-" * 20)
    option_user = input("Welcome, what do you want to do today? -> ")
    if option_user in options:
        match option_user:
            case "1": add_product()
            case "2": search_product()
            case "3": update_price()
            case "4": delete_product()
            case "5": print(f"Total inventory: {total_inventory()}")
    else:
        print("That option it's not in the menu")


menu()
#with this while the user is asked if he wants to continue in the program
while True:
    try:
        repeat_program = input("Do you want continue in the program? (Y/N): ").lower()
        if repeat_program == "y":
            menu()
        elif repeat_program == "n":
            print("Come back soon!!")
            exit()
            break
        else:
            print("INtroduce a correct letter")
    except ValueError:
        print("Introduce 'y' o 'n' ")